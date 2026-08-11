abouttostuck = ["Volkswagen", "Fiat", "Ford"]

listofcars = [
    "Bugatti", "Mustang", "Rolls Royce", "Lexus",
    "Toyota", "Ferrari", "Aston Martin", "Audi", "Nissan"
]

priceofcars = [
    1000000, 2000000, 3000000, 400000,
    5000000, 6000000, 700000, 800000, 900000
]

dict1 = dict(zip(listofcars, priceofcars))

interest = input("What brand are you looking for? ").title()

if interest in dict1:
    money = int(input("Enter the amount you have: "))

    if money >= dict1[interest]:
        balance = money - dict1[interest]
        print("The car is available.")
        print(f"The price is ₦{dict1[interest]:,}")
        print(f"You paid ₦{money:,}")
        print(f"Your balance is ₦{balance:,}")
    else:
        shortage = dict1[interest] - money
        print("You don't have enough money.")
        print(f"You need ₦{shortage:,} more.")

elif interest in abouttostuck:
    print("The car is on the way.")

else:
    print("The car is not available.")