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
