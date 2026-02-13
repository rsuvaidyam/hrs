# HRS Bakery – Feature Checklist

**Store focus:** Cakes, Cake Accessories & Sweets.

## Customer Side

| Feature | Status | Notes |
|--------|--------|--------|
| Beautiful homepage with hero banner | Done | Hero, featured products, categories (Cakes / Cake Accessories / Sweets), testimonials, gallery, footer |
| Product catalog (cakes, cake accessories, sweets) | Done | Browse by category/event; Product List + Product Details |
| Filters (eggless, vegan, gluten-free) | Done | ProductFilters on catalog; Products: is_vegan, is_gluten_free; product_type Eggless |
| Product detail page | Done | ProductDetails.vue with options, add to cart |
| Add to cart | Done | AddToCartBtn; Cart view |
| Online checkout | Done | PlaceOrder with address, payment (Cash/UPI/Card) |
| Order tracking | Done | My Order list + Order detail (OrderItem.vue) |
| Customer login/signup | Done | Login.vue, Frappe auth; Profile, logout |

### Checkout – Discount / Coupon

- Apply coupon on Place Order page (code + Apply).
- API: `validate_coupon(code, total, category)` – returns discount amount.
- Coupon Code doctype: name1, discount_mode (Percent/Rupee), discount, max_discount_in_ruppes, discount_category, status, start_on, expire_on.

---

## Admin Side (Frappe Desk)

| Feature | Status | Notes |
|--------|--------|--------|
| Product management | Done | DocType **Products** – name, category, price, product_type (Veg/Non-Veg/Eggless), is_vegan, is_gluten_free, status, images |
| Category management | Done | DocType **Category** – name1, status, description |
| Inventory | Module | App has `hrs/inventory`; extend with stock if needed |
| Order dashboard | Done | DocType **Order** (list + form); Workspace **Master** has Order shortcut |
| Customer list | Done | Use **User** list (customers = users who order); or **Hrs User** if used |
| Discount / coupon system | Done | DocType **Coupon Code**; validate in checkout |
| Daily sales report | Done | Script Report **Daily Sales** – From/To date; columns: Date, Order, Customer, Product, Item, Qty, Payment, Status |

### Enabling Daily Sales Report (Admin)

1. Go to **Desk → Report → New**.
2. Set **Report Name**: `Daily Sales`.
3. Set **Report Type**: `Script Report`.
4. Set **Module**: `hrs`.
5. Save.  
   Report script: `hrs/report/daily_sales/daily_sales.py` (and `.js` for filters).

### Main categories (Cakes, Cake Accessories, Sweets)

Create these **Category** records in Frappe so the homepage and catalog show them:

- **Cakes** – birthday cakes, custom cakes, celebration cakes  
- **Cake Accessories** – candles, toppers, party supplies  
- **Sweets** – mithai, chocolates, confections  

Use the same **Name** (or name1) as above so links like `/product-list/category/Cakes` work. Assign each **Product** to one of these categories.

### Workspace (Master)

Shortcuts: Carousel, Category, Events, Products, Order, Coupon Code, Daily Sales, State, District.

---

## Backend APIs (Customer)

- `get_event_by_product`, `get_product_details`, `products_list` (with filters), `product_search`
- `add_to_cart`, `cart_count`, `get_cart`
- `place_order`, `get_order`, `get_order_details`
- `get_address`, `add_address`, `change_address`
- `validate_coupon` (code, total, category)
- `get_featured_products`, `get_category`, `get_testimonials`, `get_gallery`, `get_site_settings`, `newsletter_subscribe`

---

## Migrate After Code Changes

- New/updated DocTypes (e.g. Products with is_vegan, is_gluten_free):  
  `bench --site [site] migrate`
- Clear cache if needed:  
  `bench --site [site] clear-cache`
