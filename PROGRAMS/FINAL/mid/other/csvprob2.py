Celsius = [39.2, 36.5, 37.3, 37.8]

Farhenheit = list(map(lambda x: (float(9) / 5) * x + 32, Celsius))
print(Farhenheit)
C = list(map(lambda x: (float(5) / 9) * (x - 32), Farhenheit))
print(C)

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
S1 = list(map(lambda x, y: x + y, a, b))
S2 = list(map(lambda x, y, z: x + y + z, a, b, c))
S3 = list(map(lambda x, y, z: x + y - z, a, b, c))
print(S1)
print(S2)
print(S3)

f = [10, 5, 6, 23, 12, 34, 54, 56, 45]
result1 = list(filter(lambda x: x % 2 != 0, f))
print(result1)
result2 = list(filter(lambda x: x % 2 == 0, f))
print(result2)

li = [5, 7, 22, 97, 54, 62, 77, 23, 73]
result = list(filter(lambda x: (x >= 25), li))
print(result)

from functools import reduce

li = [1, 2, 3, 4, 5, 6, 7]
sum = reduce((lambda x, y: x * x + y * y), li)
print(sum)

from functools import reduce

f = lambda a, b: a if (a > b) else b
r = reduce(f, [47, 111, 42, 102, 13])
print(r)
