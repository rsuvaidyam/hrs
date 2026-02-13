import frappe

class CartAPIs:
    def cart_count(usr):
        cart = frappe.db.count('Cart',filters={'owner':usr})
        return cart

    def get_cart(usr):
        cart_data = frappe.get_all('Cart', filters={'owner': usr}, fields=['name', 'product', 'count', 'msg', 'option'])

        products = []
        for cart in cart_data:
            # Option may be a Product Option name (variant) or the product name itself (simple product)
            product_names = frappe.get_all(
                'Product Option', filters={'parent': cart.product, 'name': cart.option}, pluck='name'
            )
            if product_names:
                for name in product_names:
                    products_doc = frappe.get_doc('Product Option', name)
                    image_doc = frappe.get_all(
                        'Images Child', filters={'parent': products_doc.parent}, fields=['name', 'image']
                    )
                    p_dict = products_doc.as_dict() if products_doc else {}
                    if products_doc.get('parent') and frappe.db.exists('Products', products_doc.parent):
                        p_dict['category'] = frappe.db.get_value('Products', products_doc.parent, 'category')
                    products.append({
                        'count': cart.count,
                        'product': p_dict,
                        'images': image_doc if image_doc else [],
                    })
            else:
                # Simple product: option == product name (no Product Option child)
                if frappe.db.exists('Products', cart.product):
                    product_doc = frappe.get_doc('Products', cart.product)
                    doc_dict = product_doc.as_dict()
                    image_doc = getattr(product_doc, 'images', None) or []
                    if hasattr(image_doc, '__iter__') and not isinstance(image_doc, (str, dict)):
                        image_doc = [{'name': getattr(r, 'name', None), 'image': getattr(r, 'image', None)} for r in image_doc]
                    else:
                        image_doc = doc_dict.get('images') or []
                    # Normalize to same shape as Product Option for frontend (name1, final_price, parent)
                    products.append({
                        'count': cart.count,
                        'product': {
                            'name': doc_dict.get('name'),
                            'name1': doc_dict.get('product_name'),
                            'parent': doc_dict.get('name'),
                            'price': doc_dict.get('price'),
                            'final_price': doc_dict.get('price'),
                            'discounts': 0,
                            'qty': 1,
                            'unit': 'pc',
                            'category': doc_dict.get('category'),
                        },
                        'images': image_doc,
                    })
        return products

    def add_to_cart(product, event,option):
        try:
            existing_cart = frappe.db.exists('Cart', {'option': option})
            if existing_cart:
                doc = frappe.get_doc('Cart', existing_cart)
                if event == 'plus':
                    doc.count += 1
                elif event == 'minus':
                    doc.count -= 1 
                
                if doc.count == 0:
                    doc.delete()
                    frappe.publish_realtime('cart_update', {"count": 0}, user=frappe.session.user)
                    return {"msg": "Item removed from cart", "code": "200", "data": None}
                else:
                    doc.save(ignore_permissions=True)
            else:
                doc = frappe.new_doc('Cart')
                doc.count = 1
                doc.product = product
                doc.option = option
                doc.insert(ignore_permissions=True)
            
            frappe.publish_realtime('cart_update', {"count": doc.count}, user=frappe.session.user)
            return {"msg": "Item added to cart", "code": "200", "data": doc}
        
        except Exception as e:
            return {"msg": str(e), "code": "500", "data": None}


