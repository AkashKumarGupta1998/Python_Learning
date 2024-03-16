#    --------------Functions -------------
# # -----Function for print hello world-------
# def printHello():
#      print("Hello World")

# printHello()
# #  ----add function----------
# def add(n1,n2):
#      print("n1",n1, "n2",n2)
#      sum=n1+n2
#      return sum

# x=7
# y=8
# print("The sum of no. is: ",add(x,y))
# #-------------------------or
# print("the sum of no. is : ",add(2,8))
# #---------by named argument-------
# print("the sum of no. is: ",add(n1=5,n2=8))

#----------if don't know the arguments value(Arbitary arguments)-------
# def addAllnumber(*args):
#      sum=0
#      for i in args:
#           sum += i
#      return sum
# #---calling
# output=addAllnumber(2,7,9,67)
# print("the sum of no. is:",output)

# #-------------keywarded arguments----------------
# def StudentInfo(**kwargs):
#      for x,y in kwargs.items():
#           print(x,y)

# StudentInfo(name="akash",roll=56,marks=78)

# #--------writing a function for summation----------
# def summation(n):
#      sum = 0
#      for i in range(1,n+1):
#           sum +=i
#      return sum
# n = int(input("Enter n:"))

# #call
# output=summation(n)
# print("The sum of all whole no. till n is:",output)
# # for another input
# n2=int(input("Enter n2:"))
# output2=summation(n2)
# print("The sum of no.:",output2)

# #-----nested function-------------
# def outer_function():
#      x=1   # varible is in outer function

#      def inner_function():
#           y=2 #variable for inner function
#           result=x+y
#           return result
#      return inner_function()
# output = outer_function()
# print(output)

#  --------Pass by reference and Pass by value---------
# #------pass by value
# def addone(x):
#      x=x+1
#      print("Inside function:",x)
# #---call
# x=5    #free from above value
# addone(x)
# print("outside_function:",x)

#---Pass by reference
# def modifylist(lst):
#      lst.append(4)
#      print("Inside_function",lst)

# lst=[1,2,3]
# modifylist(lst)
# print("outside_list",lst)
# #-------no change in list
# def modifylist(lst):
#      lst=[4,5,6]
#      print("Inside_function",lst)

# lst=[1,2,3]
# modifylist(lst)
# print("outside_list",lst)

################-----Built-in functions----------
# #----------factorial question----
# def factorial(n):
#      ans=1
#      if n==0:
#           ans=1
#      else:
#           for i in range(1,n+1):
#                ans*=i
#      return ans
# n = int(input("enter n:"))

# output=factorial(n)
# print("The value of factorial n is:",output)



