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
def place_order(data, coupon_code=None, coupon_discount=None):
    import json
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except Exception:
            data = []
    if not isinstance(data, list):
        data = []
    try:
        coupon_discount = float(coupon_discount) if coupon_discount is not None else 0
    except (TypeError, ValueError):
        coupon_discount = 0
    coupon_code = (coupon_code or '').strip() if coupon_code else ''
    return OrderAPIs.place_order(data, coupon_code=coupon_code, coupon_discount=coupon_discount)


@frappe.whitelist(allow_guest=True)
def validate_coupon(code, total=None, category=None):
    """Validate coupon and return discount amount. total and category optional."""
    if not code or not str(code).strip():
        return {'valid': False, 'message': 'Enter a coupon code', 'discount': 0}
    try:
        from datetime import datetime
        now = datetime.now()
        code_str = str(code).strip()
        name = frappe.db.get_value('Coupon Code', {'name': code_str}, 'name')
        if not name:
            return {'valid': False, 'message': 'Invalid coupon code', 'discount': 0}
        doc = frappe.get_doc('Coupon Code', name)
        if doc.status != 'Active':
            return {'valid': False, 'message': 'Coupon expired or inactive', 'discount': 0}
        if doc.get('start_on') and now < doc.get('start_on'):
            return {'valid': False, 'message': 'Coupon not yet valid', 'discount': 0}
        if doc.get('expire_on') and now > doc.get('expire_on'):
            return {'valid': False, 'message': 'Coupon expired', 'discount': 0}
        if category and doc.get('discount_category') and doc.discount_category != category:
            return {'valid': False, 'message': 'Coupon not valid for this category', 'discount': 0}
        try:
            total_f = float(total) if total is not None else 0
        except (TypeError, ValueError):
            total_f = 0
        if doc.discount_mode == 'Percent( % )':
            discount = total_f * (float(doc.discount or 0) / 100)
        else:
            discount = float(doc.discount or 0)
        if doc.get('max_discount_in_ruppes') and discount > doc.max_discount_in_ruppes:
            discount = doc.max_discount_in_ruppes
        discount = max(0, round(float(discount), 2))
        return {'valid': True, 'discount': discount, 'message': 'Applied'}
    except Exception as e:
        return {'valid': False, 'message': str(e) or 'Invalid coupon', 'discount': 0}
    
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

# Homepage / Featured --:--
@frappe.whitelist(allow_guest=True)
def get_featured_products(user=None):
    """Return featured products for homepage (first 8 from events)."""
    try:
        data = ProductAPIs.event_by_product(user)
        if not data:
            return []
        flat = []
        for products in data.values():
            flat.extend(products)
        return flat[:8]
    except Exception:
        return []

# Testimonials --:--
@frappe.whitelist(allow_guest=True)
def get_testimonials():
    """Return testimonials for homepage."""
    try:
        if frappe.db.table_exists('Testimonial'):
            docs = frappe.get_all(
                'Testimonial',
                filters={'published': 1},
                fields=['customer_name', 'quote', 'role', 'avatar'],
                order_by='creation desc',
                limit_page_length=10
            )
            return docs
        return []
    except Exception:
        return []

# Gallery --:--
@frappe.whitelist(allow_guest=True)
def get_gallery():
    """Return gallery images for homepage strip."""
    try:
        if frappe.db.table_exists('HRS Settings'):
            doc = frappe.get_single('HRS Settings')
            gallery = getattr(doc, 'gallery_images', None) or []
            out = []
            for d in gallery:
                img = d.get('image')
                if img:
                    out.append({'url': img, 'alt': d.get('title', '') or 'Gallery'})
            return out
        return []
    except Exception:
        return []

# Site settings (hero, footer) --:--
@frappe.whitelist(allow_guest=True)
def get_site_settings():
    """Return all site settings from HRS Settings (dynamic, no fallbacks)."""
    try:
        if frappe.db.table_exists('HRS Settings'):
            doc = frappe.get_single('HRS Settings')
            keys = (
                'site_name', 'hero_tagline', 'hero_headline', 'hero_subtext', 'hero_image',
                'featured_title', 'featured_subtext', 'categories_title', 'categories_subtext',
                'store_hours', 'address', 'footer_tagline', 'meta_title'
            )
            out = {}
            for key in keys:
                try:
                    val = getattr(doc, key, None)
                    out[key] = val if val is not None else ''
                except Exception:
                    out[key] = ''
            return out
        return {}
    except Exception:
        return {}

# Newsletter --:--
@frappe.whitelist(allow_guest=True)
def newsletter_subscribe(email):
    """Subscribe email to newsletter."""
    if not email or '@' not in str(email):
        return {'ok': False, 'message': 'Invalid email'}
    try:
        if frappe.db.table_exists('Newsletter Subscriber'):
            if frappe.db.exists('Newsletter Subscriber', {'email': email}):
                return {'ok': True, 'message': 'Already subscribed'}
            doc = frappe.new_doc('Newsletter Subscriber')
            doc.email = email
            doc.subscribed = 1
            doc.insert(ignore_permissions=True)
            return {'ok': True, 'message': 'Subscribed'}
        return {'ok': True, 'message': 'Subscribed'}
    except Exception as e:
        return {'ok': False, 'message': str(e)}



