import frappe
from hrs.controllers.product import ProductAPIs
from hrs.controllers.cart import CartAPIs
from hrs.controllers.adress import AddressAPIs
from hrs.controllers.order import OrderAPIs

# Product APIs --:--
@frappe.whitelist(allow_guest=True)
def get_event_by_product(user=None):
    return ProductAPIs.event_by_product(user)
    
@frappe.whitelist(allow_guest=True)
def get_product_details(name):
    return ProductAPIs.product_details(name)
    
@frappe.whitelist(allow_guest=True)
def products_list(data):
    return ProductAPIs.products_list(data)
    
@frappe.whitelist(allow_guest=True)
def product_search(key_word):
    return ProductAPIs.product_search(key_word)

# Cart APIs --:--
@frappe.whitelist(allow_guest=True)
def add_to_cart(product, event,option):
    return CartAPIs.add_to_cart(product, event,option)
    
@frappe.whitelist(allow_guest=True)
def cart_count(usr):
    return CartAPIs.cart_count(usr)
    
@frappe.whitelist(allow_guest=True)
def get_cart(usr):
    return CartAPIs.get_cart(usr)

# Order APIs --:--

@frappe.whitelist(allow_guest=True)
def place_order(data):
    OrderAPIs.place_order(data)
    
@frappe.whitelist(allow_guest=True)
def get_order(user):
    return OrderAPIs.get_order(user)

@frappe.whitelist(allow_guest=True)
def get_order_details(item):
    return OrderAPIs.get_order_details(item)

# Address APIs --:--
@frappe.whitelist(allow_guest=True)
def add_address(data):
    return AddressAPIs.add_address(data)

@frappe.whitelist(allow_guest=True)
def get_address(user):
    return AddressAPIs.get_address(user)

@frappe.whitelist(allow_guest=True)
def change_address(user,address):
    return AddressAPIs.change_address(user,address)

# Carousel APIs --:--
@frappe.whitelist(allow_guest=True)
def get_carousel():
    carousels = frappe.get_all('Carousel', filters={'status': 'Active'}, pluck='name')
    for name in carousels:
        carousel_doc = frappe.get_doc('Carousel', name)
    return carousel_doc

# Category APIs --:--
@frappe.whitelist(allow_guest=True)
def get_category():
    category = frappe.get_all('Category', fields=['*'])
    return category

# Event APIs --:--
@frappe.whitelist(allow_guest=True)
def get_event():
    event = frappe.get_all('Events', fields=['name','name1','image'])
    return event



