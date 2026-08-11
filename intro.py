# Indentation
# 1. Define the variables first so the script can run
var_one = "Hello"
var_two = "World"
var_three = "Python"
var_four = "Style"


# 2. Correct Function Definition (Hanging Indent)
# Notice the extra 8 spaces of indentation for the arguments.
# This prevents them from blending in with the 4-space indent of the print statement.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one, var_two, var_three, var_four)


# 3. Correct Function Call Option A (Vertical Alignment)
# Arguments on subsequent lines line up perfectly under the opening parenthesis.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# 4. Correct Function Call Option B (Hanging Indent)
# The first line ends with the parenthesis, and arguments are indented by 4 spaces.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# Define variables for conditional example
this_is_one_thing = True
that_is_another_thing = False

if (this_is_one_thing and
    that_is_another_thing):
    print("Both conditions are true")

#  operations

from operator import ge


z = 10 //3
print(z)

arth  =  10**3
print(arth)

arth = 10 == 10

print(arth)

arth =  10 != 3
print(arth)

arth = 10 > 3
print (arth)

arth = 10 < 3
print(arth)

arth = 10>=3
print(arth)

arth = 10 <= 3
print(arth)

w = '12'
x = '12'

if w == x :
 print('they are equal')

else :
   print ('they are not eqaul')

a = 10
b = 20

if a == b and a > b:
  print('they are equal') 
else:
  print('they are not equal')


price_of_goods  =20000
age =int (input("Enter your age"))
payment = float(input("Enter payment amount:"))

if not (age >= 18) and payment >= price_of_goods:
  print("Congratulations .. you can buy the goods")

else:
  print("sorry you cannot buy the goods")


# data types and operations
num_of_apples = int(input("Enter number of apples:"))
num_of_oranges = int(input("Enter number of oranges:"))
text =f" i have {num_of_apples} apples and {num_of_oranges} oranges"
print(text)
word = f"hello{num_of_apples}world"
print(word)

# # Ask the user for their age
age = int(input("Enter your age: "))

# # Now you can do math with it!
years_left = 100 - age
print(f"You will be 100 years old in {years_left} years.")

try:
    user_number = int(input("Enter a whole number: "))
    print(f"Thanks! Your number is {user_number}")
except ValueError:
    print("Oops! That wasn't a valid whole number.")
 
# Escape sequnce


text = "my name is johnpaul , i am  years old"
age = "20"
print("my name\r is johnpaul")
print("my name\n is johnpaul")
print("my name\\ is johnpaul")
print("my name\t is johnpaul")
print("my name\b is johnpaul")
print("my name\f is johnapul")
print("my name\' is johnpaul")

text = "My name is obumneme"
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])
print(len(text))
print(text[0:9:2]) #positive indexing 
print(text[-5:-2]) # negeative indexing

