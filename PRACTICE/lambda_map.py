# cube = lambda x: x*x*x

# l = [1,2,3,4,5]
# newl = list(map(cube, l))
# print(newl)


a = [1,2,3,4]
b = [1,2,3,4]
s1 = list(map(lambda x,y:x+y, a,b))
print(s1)