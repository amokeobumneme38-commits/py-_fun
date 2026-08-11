#   #Strings methods

import math
Text = "programming is hard as f**K"
text = "123"
print("upper:", Text.upper())
print("lower:", Text.lower())
print("capitalize:", Text.capitalize())
print("title:", Text.title())
print("strip:", Text.strip())
print("replace:", Text.replace("hard", "fun"))
print("split:", Text.split())
print("find 'is':", Text.find("is"))
print("startswith 'prog':", Text.startswith("prog"))
print("endswith 'K':", Text.endswith("K"))
print("count 'g':", Text.count("g"))
print("join example:", "-".join(["a","b","c"]))
print("format example:", "Hello {}".format("world"))
print(Text.casefold())
print(Text.swapcase())
print(text.isdecimal())
print(text.isdigit())
print(text.isnumeric())

# Replace the first dot and check if all remaining characters are digits
print(text.replace(".", "", 1).isdigit())  # True

for x in range(len(Text)):
    print(Text[x])
 
num1 = 20
num2 = 20.5
num3 = 20 + 5j.conjugate()
num4 = 0.5
print(num1)
print(num2)
print(num3)
print(num4)

ops = math.lcm(10 , 5)
Ops = math.gcd(10 , 5)
print(ops)
print(Ops)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 



