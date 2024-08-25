import frappe

@frappe.whitelist()
def cart_count(usr):
    cart = frappe.db.count('Cart',filters={'owner':usr})
    return cart

@frappe.whitelist()
def get_cart(usr):
    cart_data = frappe.get_all('Cart', filters={'owner': usr}, fields=['name', 'product', 'count'])

    products = []
    for cart in cart_data:
        product_names = frappe.get_all('Products', filters={'name': cart.product}, pluck='name')
        for name in product_names:
            products_doc = frappe.get_doc('Products', name)
            products.append({
                'count': cart.count,
                'product': products_doc.as_dict() if products_doc else {}
            })

    return products


