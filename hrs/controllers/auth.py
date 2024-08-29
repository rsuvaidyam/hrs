import frappe

@frappe.whitelist(allow_guest=True)
def login():
    frappe.local.login_manager.user = frappe.db.get_value("User", {"email": frappe.form_dict.username}, "name")
    frappe.local.login_manager.post_login()
    return frappe.local.response