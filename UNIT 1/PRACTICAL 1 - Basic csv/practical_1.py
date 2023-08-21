# First Row
with open("data.csv", "r") as f :
    text = f.readline()
    data = text.split(",")
    data[-1] = data[-1][:-1]
    print(data)

with open("data.csv", "w") as f :
    new_data = data[0] + "," + data[1] + "," + data[0] + " " + data[1]
    f.write(new_data)

with open("data.csv", "r") as f :
    text = f.readline()
    print(text)
