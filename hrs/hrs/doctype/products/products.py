# Copyright (c) 2024, rahul sah and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Products(Document):
    def before_save(self):
        if self.items:
            for option in self.items:
                if option.price:
                    discount_amount = (option.price * option.discounts) / 100
                    option.final_price = option.price - discount_amount
                else:
                    option.final_price = option.price
