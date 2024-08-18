# Copyright (c) 2024, rahul sah and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class HrsUser(Document):
	def after_insert(self):
		new_user = frappe.new_doc("User")
		new_user.email = self.email
		new_user.first_name = self.name1
		new_user.mobile_no = self.phone_no
		new_user.gender = self.gender
		new_user.birth_date = self.date_of_birth
		new_user.role_profile_name = self.role_profile
		new_user.user_image = self.user_image
		new_user.new_password = self.password
		new_user.insert(ignore_permissions=True)  
	
	def on_update(self):
		if self.get('localname'):
			pass
		else:
			user_doc = frappe.get_doc("User", self.email)
			roles_profiles = frappe.db.get_list("User Role Profile",filters={'parent':self.email},fields=['name','role_profile'],ignore_permissions=True)
			roles = frappe.db.get_list("Has Role",filters={'parent':self.email},fields=['name','role'],ignore_permissions=True)
			if len(roles):
				for role in roles:
					if role.role != self.role_profile:
						frappe.delete_doc("Has Role",role.name,ignore_permissions=True)
			if len(roles_profiles):
				for role_pro in roles_profiles:
					if role_pro.role_profile != self.role_profile:
						frappe.delete_doc("User Role Profile",role_pro.name,ignore_permissions=True)
			if (self.status=='Active'):
				user_doc.enabled = True
			else:
				user_doc.enabled = False
			user_doc.email = self.email
			user_doc.first_name = self.name1
			user_doc.mobile_no = self.phone_no
			user_doc.gender = self.gender
			user_doc.birth_date = self.date_of_birth
			user_doc.role_profile_name = self.role_profile
			user_doc.user_image = self.user_image
			user_doc.new_password = self.password
			user_doc.save(ignore_permissions=True)  
	
	def on_trash(self):
		if frappe.db.exists("User", self.email):
			frappe.delete_doc("User", self.email, ignore_permissions=True)
			frappe.msgprint(f"The user {self.email} has been deleted.")
		else:
			frappe.msgprint(f"The user {self.email} does not exist.")

