import os
import csv
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime
from PyPDF2 import PdfMerger

def read_order_data(filepath):
    try:
        with open(filepath,'r',newline='') as csvfile:
            reader=csv.DictReader(csvfile)
            orders=list(reader)
            print(list(reader))
            return orders
    except FileNotFoundError:
        print(f"file {filepath} not found")
    except Exception as e:
        print(f"An error occirred: {e}")
        return None
    
def calculate_total_amount(orders):
    for order in orders:
        order['Total Amount']=float(order['Quantity'])*float(order['Unit Price'])
        print(orders)
    return orders
    
def generate_invoices(orders,output_dir):
    if orders is None:
        print("order data is none")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for order in orders:
        order_id=order['Order ID']
        customer_name=order['Customer Name']
        product_name=order['Product Name']
        quantity=order['Quantity']
        unit_price=order['Unit Price']
        total_amount=order['Total Amount']

        pdffile=os.path.join(output_dir, f"Invoice_{order_id}.pdf")
        doc=SimpleDocTemplate(pdffile, pagesize=letter)
        elements=[]

        data=[
            ["Invoice Number:",order_id],
            ["Date of Purchase:", datetime.now().strftime('%Y-%m-%d')],
            ["Customer Name:",customer_name],
            ["Product Name:",product_name],
            ["Quantity:",quantity],
            ["Unit Price:",f"${float(unit_price):.2f}"],
            ["Total Amount:", f"${float(total_amount):.2f}"],
        ]

        table=Table(data, colWidths=[100,200])
        table.setStyle(TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                                   ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                                   ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
                                   ('BOTTOMPADDING',(0,0),(-1,-1),12),
                                   ]))
        elements.append(table)
        doc.build(elements)

def merge_invoices(output_dir, output_pdf):
    merger=PdfMerger()
    for filename in os.listdir(output_dir):
        if filename.endswith(".pdf"):
            pdf_file=os.path.join(output_dir, filename)
            merger.append(pdf_file)

    merger.write(output_pdf)
    merger.close()

if __name__=="__main__":
    csv_file="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\orders.csv"
    output_directory="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\orders"
    merged_pdf_file="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\orders\merged_invoices.pdf"
    order_data=read_order_data(csv_file)

    if order_data is not None:
        order_data=calculate_total_amount(order_data)
        generate_invoices(order_data,output_directory)
        merge_invoices(output_directory,merged_pdf_file)
        print("success")



    
        