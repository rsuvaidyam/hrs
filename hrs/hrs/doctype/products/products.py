# Copyright (c) 2024, rahul sah and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Products(Document):
    def before_save(self):
        items = getattr(self, "items", None)
        if not items:
            return
        for option in items:
            if getattr(option, "price", None):
                discounts = getattr(option, "discounts", 0) or 0
                discount_amount = (option.price * discounts) / 100
                option.final_price = option.price - discount_amount
            else:
                option.final_price = getattr(option, "price", None)
