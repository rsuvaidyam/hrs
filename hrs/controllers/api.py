import frappe

@frappe.whitelist(allow_guest=True)
def get_carousel():
    carousels = frappe.get_all('Carousel', filters={'status': 'Active'}, pluck='name')
    for name in carousels:
        carousel_doc = frappe.get_doc('Carousel', name)
    return carousel_doc

@frappe.whitelist(allow_guest=True)
def get_category():
    category = frappe.get_all('Category', fields=['*'])
    return category

@frappe.whitelist(allow_guest=True)
def get_event():
    event = frappe.get_all('Events', fields=['name','name1','image'])
    return event


@frappe.whitelist()
def add_to_cart(product, event,option):
    try:
        existing_cart = frappe.db.exists('Cart', {'option': option})
        if existing_cart:
            doc = frappe.get_doc('Cart', existing_cart)
            doc1 = frappe.get_doc('Products', product)   

            if event == 'plus':
                doc.count += 1
                for i in doc1.items:
                    if i.name == option:
                        i.count += 1
                        break
                doc1.count += 1
            elif event == 'minus':
                doc.count -= 1
                for i in doc1.items:
                        if i.name == option:
                            i.count -= 1
                            break
            
            doc1.save(ignore_permissions=True)
            
            if doc.count == 0:
                doc.delete()
                frappe.publish_realtime('cart_update', {"count": 0}, user=frappe.session.user)
                return {"msg": "Item removed from cart", "code": "200", "data": None}
            else:
                doc.save(ignore_permissions=True)
        else:
            doc = frappe.new_doc('Cart')
            doc.count = 1
            doc.product = product
            doc.option = option
            doc.insert(ignore_permissions=True)
            doc_p = frappe.get_doc('Products', product)   
            if event == 'plus':
                for i in doc_p.items:
                    if i.name == option:
                        i.count += 1
                        break
            elif event == 'minus':
                for i in doc_p.items:
                    if i.name == option:
                        i.count += 1
                        break
            
            doc_p.save(ignore_permissions=True)
        
        frappe.publish_realtime('cart_update', {"count": doc.count}, user=frappe.session.user)
        return {"msg": "Item added to cart", "code": "200", "data": doc}
    
    except Exception as e:
        return {"msg": str(e), "code": "500", "data": None}
