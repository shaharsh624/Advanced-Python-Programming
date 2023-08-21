with open("Dockerfile", "r") as f:
    i = 0
    while True:
        i = i + 1
        line = f.readline()
        if not line:
            break
        if i == 1:
            print(line)
