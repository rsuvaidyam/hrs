import frappe

class AddressAPIs:
    def get_address(user):
        data = {}
        address = frappe.get_all('Hrs Address', filters={'user': user}, fields=['default','name','name1','phone_no','house_name','district.name1 as district','state.name1 as state','pin_code','road_name','land_mark'])
        data['address_list'] = address
        data['default_address'] = next((addr for addr in address if addr['default'] == 1), None)
        return data
    
    def add_address(data):
        doc = frappe.new_doc('Hrs Address')
        doc.update(data)
        doc.insert()
        return doc
    
    def change_address(user,address):
        data = {}
        address = frappe.get_all('Hrs Address', filters={'user': user}, pluck='name')
        for name in address:
            if name == address:
                frappe.db.set_value('Hrs Address', address, 'default', 1)
            else:
                frappe.db.set_value('Hrs Address', name, 'default', 0)
        address_update = frappe.get_all('Hrs Address', filters={'user': user}, fields=['default','name','name1','phone_no','house_name','district.name1 as district','state.name1 as state','pin_code','road_name','land_mark'])
        data['address_list'] = address_update
        data['default_address'] = next((addr for addr in address_update if addr['default'] == 1), None)
        return data
