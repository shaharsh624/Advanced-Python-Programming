import csv

csvfile = open("data.csv", "r")

filereader = csv.reader(csvfile)

items = []
for row in filereader:
    items.append(row)

items.pop(0)

#Count no. of total food reviews and food items

food_items = []
count_reviews = 0
valid = 0
invalid = 0

for i in range(len(items)):
    # Valid and Invalid Reviews
    for x in items[i]:
        if x == '':
            invalid += 1
            break
    else:
        valid += 1
    count_reviews += 1

    for item in food_items:
        if item[0] == items[i][3]:
            break
    else:
        if items[i][3] != '':
            food_items.append([items[i][3],0,0])


#Top 3 Average rating of food

for i in range(len(items)):
    for j in range(len(food_items)):
        if(items[i][3] == food_items[j][0]):
            if items[i][4] != '':
                food_items[j][1] += 1
                avg_rating = (((food_items[j][1] - 1)*food_items[j][2]) + float(items[i][4])) / food_items[j][1]
                food_items[j][2] = round(avg_rating, 2)

sorted_data = sorted(food_items, key=lambda x: x[2], reverse=True)

# Select the top 3 highest rated foods
top_rated_foods = sorted_data[:3]


print("No. of reviews = ",count_reviews)
print("No. of Valid reviews = ",valid)
print("No. of Invalid reviews = ",invalid)
print("No. of Food items = ", len(food_items))

print("\nTop 3 highest rated foods:")
for food in top_rated_foods:
    print(f"Food: {food[0]}, Orders: {food[1]}, Average Rating: {food[2]}")

#Highest Rated food reviews

sorted_items = sorted(items, key=lambda x: x[4], reverse=True)
top_rated_item = sorted_items[:1]

print("\nHighest Rated")
for item in items:
    if item[4] == top_rated_item[0][4]:
        print(item)