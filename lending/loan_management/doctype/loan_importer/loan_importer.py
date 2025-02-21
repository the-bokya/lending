# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from typing import List

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils.csvutils import read_csv_content

from lending.loan_management.doctype.loan.loan import Loan


class LoanImporter(Document):
	def on_submit(self):

		csv_contents = read_csv_content(self.get_file())
		if len(csv_contents) < 2:
			frappe.throw(_("Empty file"))

	def get_file(self):
		file_doc = frappe.get_doc("File", {"file_url": self.csv_file})
		file = file_doc.get_content()
		return file

	def import_loans(self, csv_contents: List[str, str]):
		headers = read_csv_content[0]
		body = read_csv_content[1:]
		for line in body:
			loan_object = frappe.new_doc("Loan")
			for value, i in enumerate(line):
				field = headers[i]
				loan_object[field] = value

			self.import_loan(loan_object)

	def validate_fields(self):
		mandatory_fields = []

	def import_loan(self, loan_object: Loan):
		# steps
		# 1. generate opening GL
		# 2. generate repayment_schedule
		# 3. generate demand

		pass
