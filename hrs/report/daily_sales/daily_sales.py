# Copyright (c) 2025, HRS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
	filters = filters or {}
	columns = get_columns()
	data = get_data(filters)
	return columns, data


def get_columns():
	return [
		_("Date") + ":Date:100",
		_("Order") + ":Link/Order:120",
		_("Customer") + ":Link/User:120",
		_("Product") + ":Link/Products:150",
		_("Item") + ":Data:120",
		_("Qty") + ":Int:60",
		_("Payment") + ":Data:80",
		_("Status") + ":Data:80",
	]


def get_data(filters):
	from datetime import datetime
	date_from = filters.get("from_date")
	date_to = filters.get("to_date")
	if not date_from:
		date_from = datetime.now().strftime("%Y-%m-%d")
	if not date_to:
		date_to = date_from
	orders = frappe.get_all(
		"Order",
		filters=[
			["creation", ">=", date_from],
			["creation", "<=", date_to + " 23:59:59"],
		],
		fields=["name", "user", "product", "item", "count", "p_mode", "order_status", "creation"],
		order_by="creation desc",
	)
	out = []
	for o in orders:
		product_name = o.get("product") or ""
		item_name = o.get("item") or ""
		try:
			opt = frappe.get_doc("Product Option", item_name) if item_name else None
			item_label = opt.name1 if opt else item_name
		except Exception:
			item_label = item_name
		creation = o.get("creation")
		date_str = creation.strftime("%Y-%m-%d") if hasattr(creation, "strftime") else str(creation or "")[:10]
		out.append([
			date_str,
			o.get("name"),
			o.get("user"),
			product_name,
			item_label,
			o.get("count") or 0,
			o.get("p_mode") or "",
			o.get("order_status") or "",
		])
	return out
