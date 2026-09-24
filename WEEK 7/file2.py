import os
#  r = read
# a = append
# w = write
# x = create

f = open("names.txt","r")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("file doesnt exist")
finally:
    f.close

# Append - creates the file if it doesn't exist
f = open("names.txt", "a")
f.write("Neil")
f.close()

f = open("names.txt")
print(f.read())
f.close

# write (overwrite)
f = open("context.txt","w")
f.write("I deleted all of the context")

f =open("context.txt")
print(f.read())
f.close

# create the specified file , but returns an error if the file exists

if not os.path.exists("Johnpaul.txt"):
    f = open ("Johnpaul.txt","x")
    f.close()

# Delete a file

# avoid an error if it doesn't exist
if os.path.exists ("John.txt"):
    os.remove("John.txt")
else:
    print("The file you wish to delete does not exist")


with open("Johnpaul.txt") as f:
    content = f.read()

with open("names.tyxt", "w") as f:
    f.write(content)



# f = open("demofile.txt", "w")
# f.write( "My  name is Amoke Obumneme Johnpaul i am from Nsk Ugwuonye Umuchim ")
# f.close()


# f = open("demofile.txt","r")
# print(f.read())


# f = open("demofile2.txt", "w")
# f.write("HOW ARE YOU")
# f.close
# f = open("demofile2.txt", "r")
# print(f.read())


# if os.path.exists("demofile.txt"):
#     os.remove("demofile.txt")
# else:
#     print("the file does not exist")