import frappe
from frappe.utils import now_datetime

class OrderAPIs:
    def place_order(data):
        for item in data:
            new_doc = frappe.new_doc('Order')
            new_doc.update(item)
            new_doc.order_status = 'Confirm'
            new_doc.order_date = now_datetime()
            new_doc.shipping_status = 'Pending'
            new_doc.delivery_status = 'Pending'
            new_doc.submit()
            frappe.db.set_value('Product Option', item.get('item'), 'count', 0)
            cart_data = frappe.get_all(
                'Cart',
                filters={
                    'product': item.get('product'),
                    'option': item.get('item'),
                    'owner': item.get('user'),
                },
                pluck='name',
            )
            if cart_data:
                frappe.delete_doc('Cart', cart_data[0])
        return {"msg": "Order placed successfully", "code": "200", "data": None}

    def get_order(user):
        data = frappe.get_all('Order', filters={'user': user}, fields=['name','address','product','item','user','p_mode','creation'])
        for order in data:
            product = frappe.get_all('Product Option', filters={'parent': order.get('product'),'name':order.get('item')}, fields=['name','name1','parent'])
            images = frappe.get_all('Images Child', filters={'parent': order.get('product')}, fields=['image'])
            order['product'] = product[0]
            order['images'] = images[0]
        return data
    
    def get_order_details(item):
        order_doc = frappe.get_doc('Order', item)
        data = order_doc.as_dict()
        data['product'] = frappe.get_doc('Product Option', data.get('item'))
        data['address'] = frappe.get_doc('Hrs Address', data.get('address'))
        images = frappe.get_all('Images Child', filters={'parent': data.get('product')}, fields=['image'])
        data['images'] = images[0]
        return data
