# boolean
# comparison in boolean e.g ==, !=, <=, >=, <, >.
x = str(4)
y = "4"
z ="four"
print(x<=y)
print(bool(0))

# # logic in boolean e.g and ,or ,not

print( x==y )and( x==y)   
print(x!=y )and( x==y)
print(x !=y )  or (x!=y)
print(x==y)  and (x != y) 
print(x != y) and (x != y)
print(x==y)or(x==y)

email = "bumzy@gmnail.com"
phone = "123455-88"
username = " bumzyy"
# # Allows registration
# # if any field is filled
print(any([email,phone,username]))
print("-" * 40)


# # allows registration
# # only of all fields is filled
print(all([email ,phone ,username]))

print("-" * 40)


print(isinstance(123,int))
print(isinstance(True, str)) 

print("-" * 40)

print("Hello".endswith("o"))
print("Hello".startswith ("H "))

print("-" * 40)
# # comparision operators
print(10 == 10)
print(10 != 10)
print(7 > 3)
print(7 >= 3)
print(3 < 7)
print(7 <= 7)

print("-" * 40)
# # chain comparision
print(5 < 4 < 6  )
# is age between 18 an 30 ?
age = 20
print(18 <= age <= 30)
print("-" * 40)

# logical opertors
print(3 > 1 and 5 < 1)
print( 3 > 1 and 5 > 1)

print("-" * 40)

print(3 > 1 or 5 < 1)
print(3 > 1 or 5 > 1)

# cheack if system is under pressure
cpu_usage = 70
memory_usage = 95
print(cpu_usage> 90 or  memory_usage >90)

# checking user credentials before login
email = False
password = False
print(email and password)

# functions can return a boolean
def  myFunction():
    return True

print(myFunction())

# excute code based on the boolean answer of a funcion

def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

x  = 200
print(isinstance(x,int))