a = 300
b = 30
if b > a:
    print(" b is graeter than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is graeter than b")

#  short hand if / else
a = 200
b = 33
if a > b:
    print(" a is greater than b ")

a = 22000
b = 330
print("A") if a > b else print("B")

a = 3300
b = 330000
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("both conditions are true")

a = 300
b = 33
c = 600
if a > b or a > c:
    print("Atleast on of thecondtions is True")

# nested if statement

x = 41

if x > 10:
    print("above ten,")
    if x > 20:
        print("and also above 20")
    else:
        print("but not above 20.")

#  the pass Statement

a = 33
b = 200

if b > a:
    pass

# control structures

abouttostuck = ["Volkswagen", "Fiat", "Ford"]

listofcars = [
    "Bugatti",
    "Mustang",
    "Rolls Royce",
    "Lexus",
    "Toyota",
    "Ferrari",
    "Aston Martin",
    "Audi",
    "Nissan"
]

priceofcars = [
    1000000,
    2000000,
    3000000,
    4000000,
    5000000,
    6000000,
    7000000,
    8000000,
    9000000
]

dict1 = dict(zip(listofcars, priceofcars))

interest = input("What brand are you looking for? ").title()

if interest in dict1:
    money = int(input("Enter the amount you have: "))

    if money >= dict1[interest]:
        print("The car is available.")
    else:
        print("You don't have enough money.")

elif interest in abouttostuck:
    print("The car is on the way.")

else:
    print("The car is not available.")
