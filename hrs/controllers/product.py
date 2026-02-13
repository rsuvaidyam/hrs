import frappe


class ProductAPIs:
    def event_by_product(user=None):
        """Group products by event (if event_name exists). Returns {} when Products have no event_name."""
        try:
            products = frappe.get_all(
                'Products',
                filters={'status': 'Active'},
                fields=['name'],
                order_by='creation desc',
                limit_page_length=500
            )
            data = {}
            for p in products:
                doc = frappe.get_doc('Products', p.name)
                event_name = getattr(doc, 'event_name', None) or getattr(doc, 'events', None)
                if event_name:
                    if event_name not in data:
                        data[event_name] = []
                    data[event_name].append(doc.as_dict())
            return data
        except Exception:
            return {}

    def featured_products(limit=12):
        """Return featured products for Cake Showcase (active products, no event dependency)."""
        try:
            limit = int(limit) if limit else 12
            order = 'creation desc'
            if frappe.db.has_column('Products', 'featured'):
                # Prefer featured first, then by creation
                names = frappe.get_all(
                    'Products',
                    filters={'status': 'Active'},
                    fields=['name', 'featured'],
                    order_by='featured desc, creation desc',
                    limit_page_length=limit * 2
                )
            else:
                names = frappe.get_all(
                    'Products',
                    filters={'status': 'Active'},
                    fields=['name'],
                    order_by='creation desc',
                    limit_page_length=limit
                )
            out = []
            for p in names[:limit]:
                try:
                    doc = frappe.get_doc('Products', p.name)
                    out.append(doc.as_dict())
                except Exception:
                    continue
            return out
        except Exception:
            return []

    def product_details(name):
        doc = frappe.get_doc('Products', name)
        data = doc.as_dict()
        if doc.get('category') and frappe.db.exists('Category', doc.category):
            data['category_name'] = frappe.db.get_value('Category', doc.category, 'name1') or doc.category
        return data

    def products_list(data):
        datas = []
        data = data or {}
        filters = {'status': 'Active'}
        if data.get('event'):
            filters['events'] = data.get('event')
        elif data.get('category') and data.get('category') != 'all':
            filters['category'] = data.get('category')
        if data.get('eggless'):
            filters['product_type'] = 'Eggless'
        product_names = frappe.get_all('Products', filters=filters, pluck='name', order_by='creation desc')
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


