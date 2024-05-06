

import frappe
from esignature_app.print import get_rendered_template, get_print_format


@frappe.whitelist()
def get_print_formats(doctype):
	print_formats_list = ['']
	print_formats = frappe.db.get_all('Print Format',  filters={'doc_type':doctype}, fields=['*'], pluck='name')
	for p in print_formats:
		print_formats_list.append(p)
	return print_formats_list


@frappe.whitelist()
def get_doctypes():
	doctypes_list =['']
	doctypes =  frappe.db.get_all('DocType', fields=['*'], pluck='name')
	for d in doctypes:
		doctypes_list.append(d)
	return doctypes_list

@frappe.whitelist()
def get_doctypes_names(doctype):
	doctypes_name_list =['']
	doctypes_name  = frappe.db.get_all(doctype, fields=['*'], pluck='name')
	for d in doctypes_name:
		doctypes_name_list.append(d)
	return doctypes_name_list

@frappe.whitelist()
def get_preview(doctype, document_name, print_format):
    # return get_print_format("Sales Invoice", frappe.get_doc("Print Format","Pledge Note"))
	return get_rendered_template(
		doc=frappe.get_doc(doctype, document_name),
		name=None,
		print_format=frappe.get_doc("Print Format",print_format),
		meta=frappe.get_meta(doctype),
		no_letterhead=None,
		letterhead=None,
		trigger_print=False,
		settings=None,
  )


# from frappe.utils.print_format import get_print_settings

# @frappe.whitelist()
# def get_preview():
#     doc = frappe.get_doc(doctype, docname)
#     print_settings = get_print_settings(doc.doctype, doc.name, {'with_preview': 1})
#     html = frappe.get_print(doctype, doc.name, print_settings)
#     return html