import frappe
from hrs.controllers.product import ProductAPIs
from hrs.controllers.cart import CartAPIs
from hrs.controllers.adress import AddressAPIs
from hrs.controllers.order import OrderAPIs

DEFAULT_PAGE_LENGTH = 20

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
    return OrderAPIs.place_order(data)
    
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
    return [frappe.get_doc('Carousel', name).as_dict() for name in carousels]

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


@frappe.whitelist(allow_guest=True)
def get_homepage_content():
    return {
        "featured_products": [
            {
                "name": "Velvet Strawberry Gateau",
                "price": 980,
                "tag": "Best Seller",
                "description": "Layers of vanilla sponge, fresh berries, and cloud-light cream.",
                "image": "https://images.unsplash.com/photo-1464306076886-debede6f7917?auto=format&fit=crop&w=900&q=80",
            },
            {
                "name": "Belgian Chocolate Tart",
                "price": 760,
                "tag": "New",
                "description": "Dark chocolate ganache on a buttery almond shortcrust base.",
                "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=900&q=80",
            },
            {
                "name": "Rose Pistachio Pastry",
                "price": 420,
                "tag": "Eggless",
                "description": "Fragrant rose milk cream and roasted pistachio praline crunch.",
                "image": "https://images.unsplash.com/photo-1559620192-032c4bc4674e?auto=format&fit=crop&w=900&q=80",
            },
        ],
        "categories": [
            {"name": "Cakes", "note": "Celebration signatures in luxe finishes."},
            {"name": "Pastries", "note": "Delicate handcrafted bites for every craving."},
            {"name": "Artisan Bread", "note": "Long-fermented loaves baked every dawn."},
            {"name": "Cookies", "note": "Golden, buttery, and deeply comforting."},
        ],
        "testimonials": [
            {
                "name": "Ananya R",
                "title": "Food Stylist",
                "text": "Everything tastes as beautiful as it looks. Their pastries feel straight out of Paris.",
                "avatar": "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?auto=format&fit=crop&w=300&q=80",
            },
            {
                "name": "Rahul M",
                "title": "Loyal Customer",
                "text": "The same-day delivery is flawless and the cakes always arrive fresh and elegant.",
                "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=300&q=80",
            },
            {
                "name": "Sana K",
                "title": "Event Planner",
                "text": "Premium quality every single time. My clients now ask specifically for Aurélia desserts.",
                "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=300&q=80",
            },
        ],
        "gallery": [
            "https://images.unsplash.com/photo-1519869325930-281384150729?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1608198093002-ad4e005484ec?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1514517220017-8ce97a34a7b6?auto=format&fit=crop&w=800&q=80",
        ],
    }

# Generic DocType APIs --:--
def _parse_json(value, default=None):
    if value in (None, ""):
        return default
    return frappe.parse_json(value)

def _assert_permission(doctype, perm):
    if not frappe.has_permission(doctype, perm):
        frappe.throw(f"Not permitted to {perm} {doctype}.", frappe.PermissionError)

@frappe.whitelist()
def list_doctypes():
    _assert_permission("DocType", "read")
    return frappe.get_all(
        "DocType",
        filters={"istable": 0},
        fields=["name", "module", "custom"],
        order_by="name",
    )

@frappe.whitelist()
def get_document(doctype, name):
    _assert_permission(doctype, "read")
    return frappe.get_doc(doctype, name)

@frappe.whitelist()
def get_documents(
    doctype,
    filters=None,
    fields=None,
    limit_start=0,
    limit_page_length=DEFAULT_PAGE_LENGTH,
    order_by=None,
):
    _assert_permission(doctype, "read")
    parsed_filters = _parse_json(filters, {})
    parsed_fields = _parse_json(fields, ["name"])
    parsed_order_by = order_by or "modified desc"
    return frappe.get_all(
        doctype,
        filters=parsed_filters,
        fields=parsed_fields,
        limit_start=limit_start,
        limit_page_length=limit_page_length,
        order_by=parsed_order_by,
    )

@frappe.whitelist()
def create_document(doctype, data):
    _assert_permission(doctype, "create")
    payload = _parse_json(data, {})
    payload["doctype"] = doctype
    doc = frappe.get_doc(payload)
    doc.insert()
    return doc

@frappe.whitelist()
def update_document(doctype, name, data):
    _assert_permission(doctype, "write")
    payload = _parse_json(data, {})
    doc = frappe.get_doc(doctype, name)
    doc.update(payload)
    doc.save()
    return doc
