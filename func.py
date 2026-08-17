# # def my_function():
# #     print("Hello from a function")


# # my_function()


# # def my_function(fname):
# #     print(fname + " Refsnes")


# # my_function("Emil")
# # my_function("Tobias")
# # my_function("Linus")

# # # args


# # def my_function(*cars):
# #     print("The Toyata is" + cars[2])
# #     print("the Buggati is" + cars[1])
# #     print("The Mustang is " + cars[0])


# # my_function("20M", " 200M", " 2M")

# # # keyword argument & Kwargs


# # def my_function(car3, car1, car2):
# #     print("the fastest car is the " + car2)


# # my_function(car1="Toyota", car2="Porche", car3="Nissan")


# # def my_function(**babe):
# #     print("Her last name is " + babe["lname"])
# #     print("Her first name is " + babe["fname"])


# # my_function(fname="Nmesoma", lname="JEJE")


# # def my_function(country="Nigeria"):
# #     print("i am from " + country)


# # my_function("Belgum")
# # my_function("Sweden")
# # my_function()
# # my_function("Denmark")


# from bool import email
# from bool import password


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


# def print_name(*args, **kwargs):
#     print(args)
#     for name in args:
#         greeting = f"Hello {name}, how are you doing Today"
#         print(greeting)
#     print(kwargs)
#     for name, age in kwargs.items():
#         print(f"Hello {name}, you are {age} years old")


# phone_no = int(input("enter phone_no: "))


# def register(full_name, phone_no, password, confirmpass, email):
#     if not full_name:
#         print("Full name is requires")
#         Full_name = input("Enter your full name: ")
#     email = input("Enter email: ")
#     if "@" not in email:
#         print("enter a valid email")
#         email = input("Enter your email")

#     if not phone_no or type(phone_no) != int:
#         print("Enter a valid phone number: ")
#         phone_no = input("Enter your phone number: ")
#     password = input("enter passsword: ")
#     comfirmed_password = input("confirm password: ")
#     if not password or len(password) < 6:
#         print("password is too short")
#     elif password != comfirmed_password:
#         print("passwrod must match")
#     else:
#         print("Registration Succesful")


# register()

# # def sub():
# #     result = 6 - 3


def print_name(*args, **kwargs):
    print(args)

    for name in args:
        greeting = f"Hello {name}, how are you doing today?"
        print(greeting)

    print(kwargs)

    for name, age in kwargs.items():
        print(f"Hello {name}, you are {age} years old")


def register():
    full_name = input("Enter your full name: ")

    if not full_name:
        print("Full name is required")
        return

    email = input("Enter email: ")

    if "@" not in email:
        print("Enter a valid email")
        return

    phone_no = input("Enter your phone number: ")

    if not phone_no.isdigit():
        print("Enter a valid phone number")
        return

    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")

    if not password or len(password) < 6:
        print("Password is too short")

    elif password != confirm_password:
        print("Passwords must match")

    else:
        print("Registration Successful")


register()
