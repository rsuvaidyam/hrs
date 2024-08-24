import frappe

@frappe.whitelist(allow_guest=True)
def get_event_by_product():
    product = frappe.get_all('Product', fields=['*'])
    return product