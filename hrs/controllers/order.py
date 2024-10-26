import frappe

class OrderAPIs:
    def get_order(user):
        return frappe.get_all('Order', filters={'user': user}, fields=['*'])