from functools import reduce

#[expression for item in iterable if condition]
#create a list of squares
square= [x**2 for x in range(10)]
print(square)

#filter even number
even = [x for x in range(10) if x % 2 == 0]
print(even)

#lambda arguments: expression
add = lambda x,y: x+y
print(add(4,3))

#map function
numbers = [1,2,3,4]
square = map(lambda x: x**2, numbers)
print(list(square))

#latihan
angka = [2,4,6,8,10]
kali_tiga = map(lambda x: x*3, angka)
print(list(kali_tiga))

#PERBEDAAN
#MAP
evenList = map(lambda x: x % 2 == 0, numbers)
print(list(evenList))
#MENGHASILKAN BOOLEAN, JADI PENGONDISIAN

#FILTER
evenList = filter(lambda x: x % 2 == 0, numbers)
print(list(evenList))
#MENGHASILKAN ANGKA

#REDUCE
factorial = reduce(lambda x,y : x*y, numbers)
print(factorial)
#mengiterasi

maxSize = reduce(lambda x,y : x if x > y else y, numbers)
print(maxSize)








