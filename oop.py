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

    
    
class Car:
    wheel =4  
    def __init__(self,brand,model,year,price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = year

    def car_details(self):
        print( f"{self.brand} {self.model} {self.year} {self.price}")

car1 = Car("Toyota", "spider","2004","3M")
car2 = Car("Ford", "mustang","2002","7M")
car3 =  Car("Benz","s-class","2009","10M")
car4 = Car("BMW","X-series","2003","6M")

car1.car_details()
car2.car_details()
car3.car_details()
car4.car_details()





