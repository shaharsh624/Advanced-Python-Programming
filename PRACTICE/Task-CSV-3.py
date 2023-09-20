import os
import csv

#Getting all the csv files stored in the Sales Data folder
path_files = []
for root, dirs, files in os.walk("Sales Data"):
    for file in files:
        if ".csv" in file:
            file_path = os.path.join(root, file)
            path_files.append(file_path)

#Reading all the files in the list and appending their data in a list
n = 0
source_data = []
for x in path_files:
    if "Product_Names.csv" not in x:
        n += 1
        with open(x, "r", newline='') as fr:
            data = csv.reader(fr)
            for row in data:
                if "Product ID" not in row:
                    source_data.append(row)

#Writing all the data of the list in the file
with open("Sales Data/All Sales Data.csv", "a", newline='') as fw:
        csv_writer = csv.writer(fw)
        csv_writer.writerow(["Date","Store ID","Product ID","Quantity Sold"])
        csv_writer.writerows(source_data)

#Determing the total sales of all products
total_sales = {}
with open("Sales Data/All Sales Data.csv", "r", newline='') as fr:
    data = csv.DictReader(fr)
    for row in data:
        product = row["Product ID"]
        sales = int(row["Quantity Sold"])
        if product not in total_sales:
            total_sales[product] = sales
        else:
            total_sales[product] += sales
print(total_sales)

#Determing the top 5 products according to the sales
sorted_sales = sorted(total_sales.items(), key = lambda item: item[1], reverse = True)
print(sorted_sales[:5])

#Making a dictionary of productid and product name
product_matching = {}
with open("Sales Data/Product_Names.csv", "r", newline='') as frr:
            data_name = csv.DictReader(frr)
            for entry in data_name:
                product_ID = entry["Product ID"]
                product_name = entry["Product Name"]
                product_matching[product_ID] = product_name

#Making list for final output and printing it
summary = [[key, product_matching[key], value, value / n] for key, value in total_sales.items()]   
with open("Sales Data/Sales_Summary.csv", "w", newline='') as fw:
    final = csv.writer(fw)
    final.writerow(["Product ID", "Product Name", "Total Sales", "Average Sales"])
    for row in summary:
          final.writerow(row)