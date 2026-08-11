# # List Methods Demonstration
# # Note: Avoid using variable names like 'list' to prevent shadowing the built-in type.
# food_items = ["rice", "beans", "egg", "yam", "rice"]
# numbers = [1, 3, 5, 6, 300, 2, 0]
# names = ["john", "joe", "amanda", "ada", "chi", "chika"]

# print("Original Lists:")
# print("food_items:", food_items)
# print("numbers:", numbers)
# print("names:", names)
# print("-" * 40)

# # 1. append(x) - Adds an item to the end of the list
# food_items.append("plantain")
# print("1. append('plantain') ->", food_items)

# # 2. extend(iterable) - Appends elements from another list/iterable
# food_items.extend(["meat", "fish"])
# print("2. extend(['meat', 'fish']) ->", food_items)

# # 3. insert(i, x) - Inserts 'x' at index 'i'
# names.insert(1, "bob")
# print("3. insert(1, 'bob') ->", names)

# # 4. remove(x) - Removes first occurrence of 'x'
# food_items.remove("rice")
# print("4. remove('rice') ->", food_items)
# 6
# # 5. pop([i]) - Removes and returns item at index 'i' (default last)
# popped_name = names.pop()
# print(f"5. pop() -> Removed '{popped_name}', Remaining names: {names}")
# popped_first = names.pop(0)
# print(f"   pop(0) -> Removed '{popped_first}', Remaining names: {names}")

# # 6. index(x) - Returns index of first occurrence of 'x'
# index_of_egg = food_items.index("egg")
# print("6. index('egg') -> Index is:", index_of_egg)

# # 7. count(x) - Returns count of occurrences of 'x'
# rice_count = food_items.count("rice")
# print("7. count('rice') -> Count is:", rice_count)

# # 8. sort() - Sorts list in place
# numbers.sort()
# print("8. sort() -> Sorted numbers:", numbers)

# # 9. reverse() - Reverses list in place
# numbers.reverse()
# print("9. reverse() -> Reversed numbers:", numbers)

# # 10. copy() - Returns a shallow copy
# names_copy = names.copy()
# print("10. copy() -> Copy of names:", names_copy)

# # 11. clear() - Removes all elements
# names.clear()


# from random import randint
# my_list = [10,20,30,10]
# print(my_list)
# print(my_list[1])
# my_list[3] = 40
# print(my_list)

domains = [ 'www.google.com',
        'openai.com',
        'localhost',
        'WWW.DATAWITHBARAA.COM']

cleaned = [
    d.lower().replace('WWW.','')
    for d in domains
    if '.' in d
]
print(cleaned)


