
import csv
import json


list1 = ["Name", "Age", "city"]

list2 = ["Johnpaul", "20", "Nsukka"]

list3 = ["Nmesoma", "20", "Abia"]

listofdict = [
    {"name": "Johnpaul", "age": 20, "city": "NSk"},

    {"name": "Nmesoma", "age": 20, "city": "Abia"},

    {"name": "Jane", "age": 21, "city": "mbise"}



]

with open("file1.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(listofdict)

with open("file1.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(list1)
    writer.writerow(list2)
    writer.writerow(list3)

with open("new.json", "w") as file:
    write = json.dump(listofdict, file)


data = []
with open("new.json") as file:
    data = json.load(file)
print(data)


# def loadfile(n):
#     with open("new2.json", "w") as f:
#         new = json.dump(n, f)
#         return new
# print(loadfile(data))


for x in data:
    item = x.items()
    for x, y in item:
        print(x, y)
