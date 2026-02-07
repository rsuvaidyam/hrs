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
        data = frappe.get_doc('Products', name).as_dict()
        return data

    def products_list(data):
        datas = []
        parsed_data = frappe.parse_json(data) if data else {}
        filters = {}
        if parsed_data.get('event'):
            filters = {'events': parsed_data.get('event')}
        elif parsed_data.get('category'):
            filters = {'category': parsed_data.get('category')}
        products = frappe.get_all('Products', filters=filters, pluck='name')

        for name in products:
            product = frappe.get_doc('Products', name)
            datas.append(product.as_dict())
        return datas

    def product_search(key_word):
        datas = []
        data = frappe.get_all('Product Option',filters={'name1': ['like', '%{}%'.format(key_word)]}, fields=['parent as name'])
        for entry in data:
            product = frappe.get_doc('Products', entry.get('name'))
            datas.append(product.as_dict())
        return datas

