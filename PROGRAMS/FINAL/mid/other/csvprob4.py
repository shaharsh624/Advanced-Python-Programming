import os
import csv


def process_sales_data(filepath, productsales):  # productsales is the dictionary
    with open(filepath, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product_id = row["Product ID"]
            quantity_sold = int(row["Quantity Sold"])
            print(product_id)
            if product_id in productsales:
                productsales[product_id] += quantity_sold
            else:
                productsales[product_id] = quantity_sold


data_directory = r"D:/Fifth Sem/Advance Python/Practical - Theory/exam mid sem/csv"

productsales = {}

for root, dirs, files in os.walk(data_directory):
    for file in files:
        if file.endswith(".csv"):
            filepath = os.path.join(root, file)
            process_sales_data(filepath, productsales)

productnames = {}

with open(
    r"D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\product.csv", "r"
) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        productnames[row["Product ID"]] = row["Product Name"]

num_months = len(os.listdir(data_directory))

summary_data = []

for product_id, total_quantity_sold in productsales.items():
    product_name = productnames.get(product_id, "Unknown")
    average_quantity_sold = total_quantity_sold / num_months
    summary_data.append(
        [product_id, product_name, total_quantity_sold, average_quantity_sold]
    )

summary_data.sort(key=lambda x: x[2], reverse=True)
top_3_products = summary_data[:3]

with open("sales_summary.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        [
            "Product ID",
            "Product Name",
            "Total Quantity Sold",
            "Average Quantity Sold per Month",
        ]
    )
    writer.writerows(top_3_products)
