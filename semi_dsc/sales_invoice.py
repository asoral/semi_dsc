import frappe


@frappe.whitelist()
def get_img_url(doc):
    print(";;;;;;;;;;;",doc)

    query = frappe.db.sql("""select file_url from `tabFile`
     where attached_to_doctype = '{0}' and attached_to_name ='{1}' 
     and file_name like 'sign%' or file_name like 'Sign%' or file_name like 'SIGN%' limit 1
     """.format(doc,doc.name),as_dict=1)
    for i in query:
        return i.get("file_url")