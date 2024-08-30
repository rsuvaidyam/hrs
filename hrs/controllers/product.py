import frappe

import frappe

@frappe.whitelist(allow_guest=True)
def get_event_by_product():
    query = """
       SELECT 
            e.name AS event_name,
            e.name1 AS event_name1,
            p.name AS product_name, 
            p.name1 AS product_name1, 
            c.name1 AS category_name,
            p.category AS product_category,
            p.price AS product_price,
            p.count AS product_count,
            p.final_price AS final_price,
            p.discounts AS product_discounts,
            ic.image AS product_images
        FROM 
            `tabProducts` p
        LEFT JOIN 
            `tabImages Child` ic ON (p.name = ic.parent AND ic.parenttype = 'Products' AND ic.parentfield = 'images')
        LEFT JOIN 
            `tabCategory` c ON p.category = c.name
        INNER JOIN 
            `tabEvents` e ON p.event = e.name
    """
    result = frappe.db.sql(query, as_dict=True)
    data = {}
    for r in result:
        event_name = r.get('event_name')
        if event_name not in data:
            data[event_name] = {
                "name": r.get('event_name'),
                "name1": r.get('event_name1'),
                "products": []
            }
        product = {
            'name': r.get('product_name'),
            'name1': r.get('product_name1'),
            'category': r.get('category_name'),
            'price': r.get('product_price'),
            'count': r.get('product_count'),
            'final_price': r.get('final_price'),
            'discounts': r.get('product_discounts'),
            'images': [{"url":r.get('product_images')}] if r.get('product_images') else []
        }
        for existing_product in data[event_name]['products']:
            if existing_product['name'] == product['name']:
                existing_product['images'].extend(product['images'])
                break
        else:
            data[event_name]['products'].append(product)
    
    return list(data.values())

import frappe

@frappe.whitelist(allow_guest=True)
def get_product_details(name):
    query = """
       SELECT 
            p.name AS product_name, 
            p.name1 AS product_name1, 
            c.name1 AS category_name,
            p.category AS product_category,
            p.price AS product_price,
            p.final_price AS final_price,
            p.discounts AS product_discounts,
            p.description AS description,
            ic.image AS product_images,
            ic.name AS product_images_name
        FROM 
            `tabProducts` p
        LEFT JOIN 
            `tabImages Child` ic ON (p.name = ic.parent AND ic.parenttype = 'Products' AND ic.parentfield = 'images')
        LEFT JOIN 
            `tabCategory` c ON p.category = c.name
        WHERE
            p.name = %s
    """
    result = frappe.db.sql(query, (name), as_dict=True)
    data = {"name": None}
    
    for r in result:
        if data['name'] is None:
            data = {
                "name": r.get('product_name'),
                "name1": r.get('product_name1'),
                "category": r.get('category_name'),
                "price": r.get('product_price'),
                "final_price": r.get('final_price'),
                "discounts": r.get('product_discounts'),
                "description": r.get('description'),
                "images": [{"url":r.get('product_images'),"name":r.get('product_images_name')}] if r.get('product_images') else []
            }
        else:
            if r.get('product_images'):
                data['images'].append({"url":r.get('product_images'),"name":r.get('product_images_name')})

    return data


