import frappe

@frappe.whitelist(allow_guest=True)
def get_carousel():
    carousels = frappe.get_all('Carousel', filters={'status': 'Active'}, pluck='name')
    for name in carousels:
        carousel_doc = frappe.get_doc('Carousel', name)
    return carousel_doc

@frappe.whitelist(allow_guest=True)
def get_category():
    category = frappe.get_all('Category', fields=['*'])
    return category

@frappe.whitelist(allow_guest=True)
def get_event():
    event = frappe.get_all('Events', fields=['name','name1','image'])
    return event

@frappe.whitelist()
def add_to_cart(product):
    try:
        existing_cart = frappe.db.exists('Cart', {'product': product})
        if existing_cart:
            doc = frappe.get_doc('Cart', existing_cart)
            doc.count += 1
            doc.save(ignore_permissions=True)
        else:
            doc = frappe.new_doc('Cart')
            doc.count = 1
            doc.product = product
            doc.insert(ignore_permissions=True)
        frappe.publish_realtime('cart_update', {"count": doc.count}, user=frappe.session.user)
        return {"msg": "Item added to cart", "code": "200", "data": doc}
    except Exception as e:
        return str(e)
