# Copyright (c) 2024, rahul sah and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Products(Document):
    def before_save(self):
        if self.discounts:
            discount_amount = (self.price * self.discounts) / 100
            self.final_price = self.price - discount_amount
        else:
            self.final_price = self.price
