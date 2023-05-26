import frappe
import requests
import os

def get_passport(self,fieldname):
    settings = frappe.get_doc("Passport Settings")
    url = 'https://app.nanonets.com/api/v2/OCR/Model/' + settings.secret +'/LabelUrls/?async=false'
    path = os.getcwd()
    site = frappe.local.site
    if img:=self.get(fieldname):
        file_path = f'{path}/{site}/public{img}'
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth(settings.key, ''), files=files)
    return response.json()
