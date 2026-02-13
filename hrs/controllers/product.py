import frappe

class ProductAPIs :
    def event_by_product(user=None):
        data = {}
        products = frappe.get_all('Products', pluck='name')
        cart_data = []
        if user:
             cart_data = frappe.get_all('Cart', filters={'owner': user}, fields=['product', 'count','option'])
        
        for name in products:
            product = frappe.get_doc('Products', name)
            
            if not data.get(product.event_name):
                data[product.event_name] = [product]
            else:
                data[product.event_name].append(product)
        return data

    def product_details(name):
        doc = frappe.get_doc('Products', name)
        data = doc.as_dict()
        if doc.get('category') and frappe.db.exists('Category', doc.category):
            data['category_name'] = frappe.db.get_value('Category', doc.category, 'name1') or doc.category
        return data

    def products_list(data):
        datas = []
        filters = {'status': 'Active'}
        if data.get('event'):
            filters['events'] = data.get('event')
        elif data.get('category') and data.get('category') != 'all':
            filters['category'] = data.get('category')
        if data.get('eggless'):
            filters['product_type'] = 'Eggless'
        product_names = frappe.get_all('Products', filters=filters, pluck='name')
        for name in product_names:
            try:
                product = frappe.get_doc('Products', name)
                doc_dict = product.as_dict()
                if data.get('vegan') and not doc_dict.get('is_vegan'):
                    continue
                if data.get('gluten_free') and not doc_dict.get('is_gluten_free'):
                    continue
                datas.append(doc_dict)
            except Exception:
                pass
        return datas

    def product_search(key_word):
        datas = []
        data = frappe.get_all('Product Option',filters={'name1': ['like', '%{}%'.format(key_word)]}, fields=['parent as name'])
        for name in data:
            product = frappe.get_doc('Products', name)
            datas.append(product.as_dict())
        return datas


