
from functools import reduce
# def x(a): return a + 10


# print(x(5))


# def myfunc(n):
#     return lambda a:  a * n


# # mydoubler = myfunc(2)
# # print(mydoubler(11))


# def z(x, y): return x * y


# print(z(10, 6))

# def z(x, y): return x + y


# print(z(4, 6))


# multiple = lambda x: x*2
# print(multiple(4))


# add = lambda x, y: x + y
# print(add(1, 2))

# check = lambda i : i in "python"
# print(check('z'))

# prices = ['$10.99 ','$20','$30','$40','$50','$60','$70']
# print(list(map(lambda p: float(p.replace('$','')), prices)))

# p = '$10'
# print((float(p.replace('$',''))))



# prices  = [120, 30, 320, 80]

# print(list(filter(lambda p: p >=100, prices)))


# students = [['Johnpaul', 50],
#            ["Kumar", 90],
#            ['Max', 90],
#            ['Monica', 60]]

# print(list(filter(lambda row: row[1] >70, students)))

# print(list(filter(lambda row: row[0].startswith('M'),students)))
# print(students[2][0].startswith("M"))
# print(students[2][1] > 70)


# def add(n, b):
#     """Return the square of a given number n."""
#     print(n)
#     return n ** 2

# z = lambda x,y: x + 10
# s = lambda a: a.upper() if type(a) == str else a
# print(z(4,6))
# print(s("zarrm"))


# a = ["apple", "banana", "cherry", "kiwi", "grape"]
# b = filter(lambda w: len(w) > 5, a)
# print(list(b))


# strings = ["hi","hello","low", "high"]
# numbers = tuple(range(2,10))
# convertstrings = list(map(add, numbers))
# print(convertstrings)
# print(numbers)

# evens = lambda x: x % 2 == 0

# hashi = lambda x: x if "h" in x else None
# convertstrings = list(filter(evens, numbers))
# convertstrings = list(filter(hashi, strings))
# print(convertstrings)

# varreduce = reduce(add, numbers)
# print(varreduce)


# x = lambda a : a + 10
# print(x(5))

# def myfunc(n):
#     return lambda a : a * n

# mydoubler = myfunc(2)
# print(mydoubler(9000))

my_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(lambda x : x**2  ,my_number))
print(squares)

evens = list(filter(lambda x : x % 2 == 0, my_number))
print(evens)


values = [(1, 'b', "hello"), (2, 'a', "world"), (3, 'c',"johnpaul")]
sorted_values = sorted(values, key = lambda x: x[1] + x[2])
print(sorted_values)


numbers =[1, 2, 3, 4, 5]

sum_of_numbers = reduce(lambda acc, x: acc + x, numbers)
print(sum_of_numbers)


max_value = reduce(lambda acc, x: acc if acc > x else x, numbers)
print(max_value)


