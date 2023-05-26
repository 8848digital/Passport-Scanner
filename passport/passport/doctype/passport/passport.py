import frappe
import json
from frappe.model.document import Document
from passport.passport.API.passport_api import get_passport

class Passport(Document):
	def validate(self ,method=None):
		if self.has_value_changed("scan_image1") and (self.scan_image1 == 1):
			print("Running for scan_image1")
			self.visiting_data("image1")

	def visiting_data(self, fieldname):
		print("***")
		try:
			doc_name = self.name
			print("Name",doc_name)
			response = get_passport(self, fieldname)
			frappe.logger('scanner').exception(response)
			data = response['result']
			print("data",data)
			pred = data[0]['prediction']
			for i in pred:
				self.append("passport_data",{
				"label" : i['label'],
				"ocr_text" : i['ocr_text']
			})
		except Exception as e:
			frappe.logger('scanner').exception(e)


	
	
			