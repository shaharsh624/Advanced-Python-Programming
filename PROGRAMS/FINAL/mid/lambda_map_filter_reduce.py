# cube = lambda x: x*x*x

# l = [1,2,3,4,5]
# newl = list(map(cube, l))
# print(newl)

# a = [1,2,3,4]
# b = [1,2,3,4]
# s1 = list(map(lambda x,y:x+y, a,b))
# print(s1)

# a = [1,2,3,4,5]
# s2 = list(filter(lambda x:x>2, a))
# print(s2)

# from functools import reduce
# num = [1,2,3,4,5]
# sum = reduce(lambda x,y : x+y, num)
# print(sum)

# Find max in an array
from functools import reduce 
f=lambda a,b: a if(a>b) else b
r = reduce(f, [47,111,42,102,13])
print(r)
