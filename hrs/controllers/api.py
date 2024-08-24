import frappe

@frappe.whitelist(allow_guest=True)
def get_carousel():
    carousels = frappe.get_all('Carousel', filters={'status': 'Active'}, pluck='name')
    for name in carousels:
        carousel_doc = frappe.get_doc('Carousel', name)
    return carousel_doc
