import frappe

@frappe.whitelist()
def cart_count(usr):
    cart = frappe.db.count('Cart',filters={'owner':usr})
    return cart
