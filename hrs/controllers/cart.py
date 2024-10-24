import frappe

@frappe.whitelist()
def cart_count(usr):
    cart = frappe.db.count('Cart',filters={'owner':usr})
    return cart

@frappe.whitelist()
def get_cart(usr):
    cart_data = frappe.get_all('Cart', filters={'owner': usr}, fields=['name', 'product', 'count','msg','option'])

    products = []
    for cart in cart_data:
        product_names = frappe.get_all('Product Option', filters={'parent': cart.product,'name':cart.option}, pluck='name')
        for name in product_names:
            products_doc = frappe.get_doc('Product Option', name)
            image_doc = frappe.get_all('Images Child', filters={'parent': products_doc.parent}, fields=['name','image'])
            products.append({
                'count': cart.count,
                'product': products_doc.as_dict() if products_doc else {},
                'images': image_doc if image_doc else [],
            })

    return products


