

# def my_function():
#     print("Hello from a function")


# my_function()


# def my_function(fname):
#     print(fname + " Refsnes")


# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# # args


# def my_function(*cars):
#     print("The Toyata is" + cars[2])
#     print("the Buggati is" + cars[1])
#     print("The Mustang is " + cars[0])


# my_function("20M", " 200M", " 2M")

# # keyword argument & Kwargs


# def my_function(car3, car1, car2):
#     print("the fastest car is the " + car2)


# my_function(car1="Toyota", car2="Porche", car3="Nissan")


# def my_function(**babe):
#     print("Her last name is " + babe["lname"])
#     print("Her first name is " + babe["fname"])


# my_function(fname="Nmesoma", lname="JEJE")


# def my_function(country="Nigeria"):
#     print("i am from " + country)


# my_function("Belgum")
# my_function("Sweden")
# my_function()
# my_function("Denmark")


# def my_function(food):
#     for x in food:
#         print(x)


# fruits = ["apple", "pineapple", "banana", "peach"]

# my_function(fruits)


# def my_function(x):
#     return 20 * x


# print(my_function(20))
# print(my_function(10))
# print(my_function(5))
# print(my_function(7))


# def tri_recursion(k):
#     if (k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result


# print("\n\nRecursion Example Results")
# tri_recursion(6)


# def sub():
#     result = 6 - 3


# def start_day():
#     print("Wake up")
#     print("Pray")
#     print("Brush teeth")
#     print("work out")
#     print("take a shower")


# start_day()


# x = 50


# def add():

#     if not x:
#         return "X has no value"
#     return x


# def sub():
#     result = x-3
#     return result


# print(add())

# print(sub())

# f = 2


# def multiple_factor(x):
#     y = x * f
#     print(y)


# multiple_factor(3)


case_rule = "lower"


def clean_name(first_name, last_name, country):
    first = first_name.strip()
    last = last_name.strip()
    full_name = first + "" + last
    print(full_name, "From", country)


clean_name("  Johnpaul  ", "  Amoke  ", " Nsk ")  # positional

clean_name(first_name=" Amoke ", last_name=" Johnpaul ",
           country=" NSk ")  # key words


# calc the tota; of values
def total(a, b):
    print(a + b)
