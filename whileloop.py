# i = 1
# while i < 6:
#     print(i)
#     i += 1
# print('-'* 40)

# # break stemenet
# i = 1
# while i < 6:
#   print(i)
#   if (i == 3):
#     break
#   i += 1
# print('-'* 40)

# # continue statement

# i = 0
# while i < 6:
#     i += 1
#     if i == 1:
#         continue
#     print(i)
# print('-'* 40)

# #  else statement

# i = 1 
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no onger less than 6")

# count = 1
# while count <= 50:
#     print(count)
#     count += 2

# answer = ""
# while answer != "yes":
#     answer  = input("Do you agree?(yes/ no)")
# print("thank you")

attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we are on the same page")
        break
    attempts += 1
else:
 print("3 stricks you are out")