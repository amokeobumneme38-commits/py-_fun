# thisdict = {
# "brand": "toyota",
# "model": "camry",
# "year" : "2020"
#  }
# print(thisdict)
# print("-" * 40)

# #  accessing items

# thisdict = {
# "brand": "toyota",
# "model": "camry",
# "year" : "2020"
#  }
# x = thisdict["model"]
# print(x)
# print(thisdict["year"])
# print("-" * 40)


# thisdict = {
# "brand": "toyota",
# "model": "camry",
# "year" : "2020"
#  }

# x = thisdict.get("brand")
# print(x)
# print("-" * 40)

# # changing values
# thisdict["year"] = 2024
# print(thisdict)
# print("-" * 40)
# #  loop 

# for x in thisdict:
#     print(x)
# print("-" * 40)
# # print all values

# for x in thisdict:
#     print(thisdict[x])
# print("-" * 40)
# # using the method value to return the values of the dictionary

# for x in thisdict.values():
#     print(x)
# print("-" * 40)
# # loop through both keys and values by using the items()method
# for x , y in thisdict.items():
#     print(x, y)
# print("-" * 40)

# # check if keys exist
# if "model" in thisdict:
#     print("yes")
# print("-" * 40)

# #  length method
# print(len(thisdict))
# print("-" * 40)

# #  adding items
# thisdict["color"] = "red"
# print(thisdict)
# print("-" * 40)

# # #  removing items
# # thisdict.pop("model")
# # print(thisdict)
# # print("-" * 40)

# # thisdict.popitem()
# # print(thisdict)
# # print("-" * 40)
# # del and clear empties the dictionary

# # mydict = thisdict.copy()
# # print(mydict)

# # mydict = dict(thisdict)
# # print(mydict)

# myfamily = {
#     "child1" : {
#         "name" : "obumneme",
#         "year" : 2006
#     },
#     "child2" : {
#         "name" : "chilieoma",
#         "year" : 2009
#     },
#     "child3" : {
#         "name" : "oyieze",
#         "year" : 20013

#     }

# }
# print(myfamily)

# old_prices = {'apple': 1.0, 'banana': 0.5, 'kiwi': 1.5}
# new_prices = {item: price * 2 for item, price in old_prices.items()}
# print(new_prices)


AGE =  20
print(18 <= AGE <=30)