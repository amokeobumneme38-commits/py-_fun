# class Student:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
    
#     def introduce(self):
#         print(f"Myname is {self.name} and i am {self.age} years old.")
        

# student1 = Student("John", 20)
# student2 = Student("Ada", 21)

# student1.introduce()
# student2.introduce()



# class Pythonstudent:
#     course = "Python"
#     def __init__(self, name, age, mail, height):

#         self.name = name
#         self.age = age
#         self.mail = mail
#         self.height = height

# student = Pythonstudent("John", "20", "email@email.com", "5.9")
# students = Pythonstudent("James", "22", "oma@email.com","6.7")

# print(student.age)
# print(student.name)
# print(student.course)

# print("\t")

# print(students.age)
# print(students.name)
# print(students.course)

    
    


# class Myclass:
#     x = 5
# print(Myclass)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Wasup bicth" + self.name)
# p1 = Person("John",20)
# p1.myfunc()




# class Car:
#     # Class attribute (shared by all instances)
#     wheels = 4

#     # Constructor - runs when a new object is created
#     def __init__(self, brand, model, year):
#         self.brand = brand      # instance attribute
#         self.model = model
#         self.year = year
#         self.speed = 0

#     # Instance method
#     def accelerate(self, amount):
#         self.speed += amount
#         print(f"{self.brand} {self.model} is now going {self.speed} km/h")

#     # Another method
#     def describe(self):
#         return f"{self.year} {self.brand} {self.model}"


# # Creating objects (instances)
# car1 = Car("Toyota", "Camry", 2022)
# car2 = Car("Honda", "Civic", 2023)


# car1.accelerate(50)
# print(car1.describe())


# car1.accelerate(50)
# Python actually interprets this as:
# Car.accelerate(car1, 50)
# 'self' inside the method becomes car1


# class John:
#     total_babes = 1

#     def __init__(self, girlfriend):
#         self.girlfriend = girlfriend
#         John.total_babes += 0 

#     @classmethod
#     def get_total_babes(cls):
#         return cls.total_babes

#     @classmethod
#     def from_string(cls, john_string):
#         name =john_string.split("-")[0]
#         return cls(name)

# gf1 = John("NMESOMA")

# gf2 = John.from_string("jeje-2006-26")

# print(John.get_total_babes())


# class MathHelper:
#     @staticmethod
#     def add(a, b):
#         return a + b
# print(MathHelper.add(3, 9))

# # Encapsulation

# class Account:
#     def __init__(self, balance):
#         self.owner = "John" #public
#         self._balance = balance #private(convention)
#         self.__pin = 1234 #private(name-mangled)
# acc = Account(100000)
# print(acc.owner) # OK - public
# print(acc._balance)

# # print(acc.__pin)
# print(acc._Account__pin)



# class Account:
#     def __init__(self,balance):
#         self._balance = balance

#     @property
#     def balance(self, balance):
#         return self._balance

#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError ("Balance cannot be negative")
#         self._balance = value
# acc = Account(10000)
# print(acc._balance)
# acc.balance = 20000
# # acc.balance = -50

# # inheritance

# class Vehicle:
#     def __init__(self,brand):
#         self.brand = brand

#     def honk(self):
#         print("honk honk bitch")

# class Car(Vehicle):
#     def __init__(self,brand, doors):
#        super().__init__(brand)
#        self.doors = doors
    
#     def describe(self):
#         return f"{self.brand} car with {self.doors} doors"
# my_car = Car ("Toyota", 4)
# my_car.honk()
# print(my_car.describe())




#method overriding

class Vehicle:
    def honk(self):  
        print("Generic beep")

class Car(Vehicle):
    def honk(self):  #overrides vehicle.honk
        print("car horn: HOONK!" )
class Bicycle(Vehicle):
    def honk(self):    #Overrides Vehocles.honk differently
        print("bicycle bell : Ring ring")

Car().honk()
Bicycle().honk()


#multiple inheritance and MRO

class Flyable:
    def move(self):
        print("Flying")
class Swimmable :
    def move(self):
        print("swimming")

class Duck(Flyable, Swimmable):
    pass
Duck().move()
print(Duck.__mro__)


class Dog:
    def speak (self):
        return "woof"
class Cat:
    def speak(self):
        return "Meow"
class Cow:
    def speak(self):
        return "Mooo"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())



class Point:
    def __init__(self,x,y):
        self.x, self.y = x , y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Point ({self.x}, {self.y})"
p1 = Point(1,2)
p2 = Point(3,4)
print(p1 + p2)

