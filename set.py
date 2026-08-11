
thisset = {"apple","banana","cherry", "kiwi"}

for x in thisset:
    print(x)

print("kiwi" in thisset)

thisset.add("orange")

print(thisset)

thisset.update(["orange", "tangerine", "grapes", "strawbeery", "berry"])
print(thisset)

print(len(thisset))

thisset.remove("banana")

print(thisset)

thisset.discard("berry")

print(thisset)

x =thisset.pop()

print(x)

print(thisset)

# del thisset

# print(thisset)
#
thisset.clear()

# print(thisset)

set1 = {"a","b","c","d","e"}
set2 = {1, 2, 3, 4, 5,}

set3 = set1.union(set2)
print(set3)

x = {"apple", "banana", "cherry","mango,", "kiwi"}
y = {"google", "microsoft", "apple","peach"}

z = x.difference(y)

print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple", "peach"}

x.difference_update(y)

print(x)

cars = { "toyota", "benz", "citron", "honda"}

cars.discard("benz")

print(cars)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

