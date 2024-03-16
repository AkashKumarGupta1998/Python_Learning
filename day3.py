# Math Case
# # making a calculator using match case
# num1 = int(input("Enter number 1"))
# num2 = int(input("Enter number 2"))

# operator = input("Enter operator")

# match operator:
#      case "+":
#           print("Sum is ",num1+num2)
#      case "-":
#           print("Difference is ",num1-num2)
#      case "*":
#           print("Product is ",num1*num2)
#      case "/":
#           print("Quotient is",num1/num2)
#      case _:
#           print("Enter a valid operator")

# Ternary operator
# in normal case
#          --------------------------- Not completed
# raining=bool(input("raining?? Plzz enter True or False"))
# #raining
# if raining==True:
#      print("Take umbrella")
# else:
#      print("Leave umbrella")
#           -------------------------------------

# num = int(input("Enter a positive numbar here"))

# output = "Even" if num%2==0 else "Odd"
# print("Output is ",output)

#     ---------------Loops--------------
#   --------for loop---------
# for i in range(1,11):
#      print(i,"akash")
#      print(1,9,2)
# for i in range(1,11,2):
#      print(i,"kumar")

# print elements of a list for loop
# list = [2,7,5,34,89]
# for i in list:
#      print(i)

# list = ["apple","banana","Guava","mango"]
# for i in list:
#      print(i)

#   -------while loop--------
# i = 2
# while i < 101:
#      print(i)
#      i += 2

#      -----------predict the output first and then run
# j = 0
# while j <= 10:
#      print(j)
#      j=j+1
#     --------or--------
# x = 1
# while x ==1:
#      x=x-1
#      print(x)
# #      ------or-------
# i = 10
# while i == 20:                           #never give output bcoz i will never be equal to 20
#      print("computer buff")

#           -----------------
# x = 4
# y = 0
# while x>=0:
#      x -= 1
#      y += 1

#      if x ==y:
#           continue
#      else:
#           print(x,y)
#  ------
# x = 4
# y = 0
# while x>=0:
#      if x == y:
#           break
#      else:
#           print(x,y)

#      x -= 1
#      y += 1

# -----------------Pattern Questions------------------
# n = int(input("Enter n: "))
# for _ in range(n):
#      print("*" * 5)

#      ---------printing given pattern --------
# for n = 4                        for n = 6
#   1234                             123456
#   1234                             123456
#   1234                             123456
#   1234                             123456
#                                    123456
#                                    123456

# n = int(input("Enter n:"))
# for i in range(n):         # for row
#      for j in range(1,n+1):           # for column
#           print(j,end="")
#      print()  
#     print given pattern
# for n = 4
# 1
# 1 2
# 1 2 3
# 1 2 3 4
n = int(input("Enter n:"))
for i in range(1,n+1):
     for j in range(1,i+1):
          print(j,end="")
     print()

#    --------print the given pattern--------------
# for n = 4
# A
# A B 
# A B C 
# A B C D

#         ---------print the given pattern----------------
     #        1
     #       123
     #      12345
     #     1234567

# n = int(input("Enter n:"))
# for i in range(1,n+1):
#      print(" " * (n-i),end="")

#      for j in range(1,2*i):
#           print(j,end="")
#      print()
