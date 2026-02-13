import frappe

def _get_line_total(product, item, count):
    """Get line total (price * count) for an order line."""
    if frappe.db.exists('Product Option', item):
        doc = frappe.get_doc('Product Option', item)
        price = float(doc.get('final_price') or doc.get('price') or 0)
    elif frappe.db.exists('Products', product):
        doc = frappe.get_doc('Products', product)
        price = float(doc.get('price') or 0)
    else:
        price = 0
    return round(price * int(count or 0), 2)


class OrderAPIs:
    def place_order(data, coupon_code=None, coupon_discount=None):
        try:
            discount_total = float(coupon_discount or 0)
        except (TypeError, ValueError):
            discount_total = 0
        coupon_str = (coupon_code or '').strip() if coupon_code else ''
        is_first = True
        for item in data:
            new_doc = frappe.new_doc('Order')
            new_doc.update(item)
            line_total = _get_line_total(item.get('product'), item.get('item'), item.get('count'))
            new_doc.total_amount = line_total
            if coupon_str:
                new_doc.coupon_code = coupon_str
            if is_first and discount_total > 0:
                new_doc.discount_amount = discount_total
                new_doc.amount_payable = max(0, round(line_total - discount_total, 2))
            else:
                new_doc.discount_amount = 0
                new_doc.amount_payable = line_total
            is_first = False
            new_doc.submit()
            if frappe.db.exists('Product Option', item.get('item')):
                frappe.db.set_value('Product Option', item.get('item'), 'count', 0)
            cart_data = frappe.get_all(
                'Cart',
                filters={'product': item.get('product'), 'option': item.get('item')},
                pluck='name',
            )
            if cart_data:
                frappe.delete_doc('Cart', cart_data[0])
        return {"msg": "Order placed successfully", "code": "200", "data": None}

    def get_order(user):
        data = frappe.get_all(
            'Order',
            filters={'user': user},
            fields=['name', 'address', 'product', 'item', 'user', 'p_mode', 'creation', 'coupon_code', 'discount_amount', 'total_amount', 'amount_payable'],
        )
        for order in data:
            product_list = frappe.get_all(
                'Product Option',
                filters={'parent': order.get('product'), 'name': order.get('item')},
                fields=['name', 'name1', 'parent'],
            )
            images = frappe.get_all('Images Child', filters={'parent': order.get('product')}, fields=['image'])
            if product_list:
                order['product'] = product_list[0]
            else:
                # Simple product: no Product Option, order.item is product name
                if frappe.db.exists('Products', order.get('product')):
                    doc = frappe.get_doc('Products', order.get('product'))
                    order['product'] = {
                        'name': doc.name,
                        'name1': doc.product_name,
                        'parent': doc.name,
                    }
                else:
                    order['product'] = {'name': order.get('product'), 'name1': '', 'parent': order.get('product')}
            order['images'] = images[0] if images else {}
            # Ensure discount/amount fields exist for UI (fallback if columns missing or old orders)
            if order.get('total_amount') is None and order.get('product') and order.get('count') is not None:
                order['total_amount'] = _get_line_total(order.get('product'), order.get('item'), order.get('count'))
            if order.get('amount_payable') is None:
                order['amount_payable'] = order.get('total_amount') or 0
            if order.get('discount_amount') is None:
                order['discount_amount'] = 0
        return data
    
    def get_order_details(item):
        order_doc = frappe.get_doc('Order', item)
        data = order_doc.as_dict()
        product_name = data.get('product')
        item_name = data.get('item')
        if frappe.db.exists('Product Option', item_name):
            data['product'] = frappe.get_doc('Product Option', item_name).as_dict()
        elif frappe.db.exists('Products', product_name):
            doc = frappe.get_doc('Products', product_name)
            data['product'] = {
                'name': doc.name,
                'name1': doc.product_name,
                'parent': doc.name,
                'price': doc.price,
                'final_price': doc.price,
            }
        else:
            data['product'] = {'name': product_name, 'name1': '', 'parent': product_name}
        if frappe.db.exists('Hrs Address', data.get('address')):
            data['address'] = frappe.get_doc('Hrs Address', data.get('address')).as_dict()
        else:
            data['address'] = {}
        images = frappe.get_all('Images Child', filters={'parent': product_name}, fields=['image'])
        data['images'] = images[0] if images else {}
        # Ensure discount/amount fields for UI
        if data.get('total_amount') is None and product_name and data.get('count') is not None:
            data['total_amount'] = _get_line_total(product_name, item_name, data.get('count'))
        if data.get('amount_payable') is None:
            data['amount_payable'] = data.get('total_amount') or 0
        if data.get('discount_amount') is None:
            data['discount_amount'] = 0
        return data