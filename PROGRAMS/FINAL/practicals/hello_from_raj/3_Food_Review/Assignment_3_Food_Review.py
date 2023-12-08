import csv
from collections import Counter

fileName = "E:/Just Code/PDEU Labs/5th Sem/Advance_Python Lab/Practical Classes/Practical_2/review.csv"

with open(fileName, newline='') as csvfile:
    csvfile = csv.reader(csvfile)
    next(csvfile)

    total = 0
    validcount = 0
    invalidcount = 0
    uniqueFoodItems = set()
    valid_reviews = []

    allRatings = []
    allData = []

    for row in csvfile:
        list = []

        for i in row:
            list.append(i)

        allRatings.append(list[4])
        allData.append(list)

        total = total+1
        uniqueFoodItems.add(list[2])

        if (list[5] != ''):
            validcount = validcount+1
            valid_reviews.append(list)
        else:
            invalidcount = invalidcount+1

        print(list)

    ratings = dict()
    for items in uniqueFoodItems:
        rat = []
        # print(items)
        for data in valid_reviews:
            if (data[2] == items):
                rat.append(float(data[4]))

        # print(rat)

        sum = 0
        for i in rat:
            sum += i

        if (sum != 0):
            average = sum/len(rat)
        else:
            average = 0

        ratings[items] = average
    # print(ratings)

    # PRINTING ALL THE STUFFS
    # print(unique_food_items)
    print("\nTotal Food Items: ", (len(uniqueFoodItems)))
    print("Total Reviews: ", total)
    print("Valid Reviews: ", validcount)
    print("Invalid Reviews: ", invalidcount)

    k = Counter(ratings)
    highest3 = k.most_common(3)
    # print(highest3)

    print("\nTop 3 Highest Rated Average of Food Items is: ")
    for i in highest3:
        print("\t",  i[0], ": ", i[1])

    print("\nDetails of Highest Rated Food Item are: ")

    maxRating = 0
    for data in allData:
        if (float(data[4]) > float(maxRating)):
            maxRating = data[4]

    for data in allData:
        if (maxRating == data[4]):
            print(data)
