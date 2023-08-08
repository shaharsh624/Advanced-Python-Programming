import csv

'''
# Total number of reviews
# Method 1
count = 0
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # print(row)
        try:
            if int(row[0]) > count:
                count = int(row[0])
        except ValueError:
            continue

print("Total number of reviews:", count)


# Method 2
count = 0
with open("data.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(row)
        if int(row['No ']) > count:
            count = int(row['No '])

print(count)
'''

'''
# Total number of Food_Items
count = 03
food_items = []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        try:
            if type(int(row[0])) == int:
                if row[2] not in food_items:
                    food_items.append(row[2])
                    count += 1
            else:
                continue
        except ValueError:
            continue

print("Total number of food items:", count)
# print(food_items)
'''



# Count Total Valid & Invalid reviews

valid_count = 0
invalid_count = 0
invalid_list = []
with open("data.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        keys = list(row.keys())
        # print(row)
        count = 0
        for key in keys:
            # print(row[key])
            if row[key] != '':
                count += 1

        if count == 6:
            valid_count += 1
        else:
            d = (int(row['No']))
            print(row.keys()[row.values().index(d-1)])
            # row.pop(row.keys()[row.values().index(d-1)])
            # print(str(d))
            invalid_count += 1

print(": ", invalid_list)
print("Valid Reviews: ", valid_count)
print("Invalid Reviews: ", invalid_count)

# food_items = {}
# with open("data.csv", 'r') as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         key = (row['Food_Id'])
#         food_items[key] = float(row['Rating'])
#     print(food_items)
#
