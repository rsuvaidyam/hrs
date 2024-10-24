import frappe

class ProductAPIs :
    def event_by_product():
        data = {}
        products = frappe.get_all('Products', pluck='name')
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
        filters={}
        if data.get('event'):
            filters= {'events':data.get('event')}
        elif data.get('category'):
            filters={'category':data.get('category')} 
        products = frappe.get_all('Products',filters=filters ,pluck='name')

        for name in products:
            product = frappe.get_doc('Products', name)
            datas.append(product.as_dict())
        return datas


