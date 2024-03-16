#---------Recursion------------
# def factorial(n):
#      # base case
#      if n==0:
#           return 1
#      # recursive case
#      ans = n*factorial(n-1)
#      return ans
# n=int(input("Enter n:"))
# print("The value of factorial n is:",factorial(n))

#------------print no. from n to 1---------
# def n21(n):
#      if n==0:
#           return
#      print(n)
#      ans=n21(n-1)
#      return ans
# n=int(input("enter n:"))
# print("all backward no is:",n21(n))
# # -----if want to print orderwise
# def n21(n):
#      if n==0:
#           return
#      ans=n21(n-1)
#      print(n)
# n=int(input("enter n:"))
# print("all backward no is:",n21(n))

#-------find sum of all whole no
# def sumall(n):
#      if n==1:
#           return 1
#      ans=n+sumall(n-1)
#      return ans
#      print(ans)

# n=int(input("Enter n:"))
# print("The sum of all whole no is:",sumall(n))

#----------calculating power--------
# def power(a,b):
#      if b==0:
#           return 1
#      ans=a*power(a,b-1)
#      return ans
#      print(ans)

# a=int(input("enter base a:"))
# b=int(input("enter power b:"))
# print(power(a,b))

#-----------fibonacci sequence------------
#----finding nth term of fibonacci sequence-----------
def fibonacci(n):
     if n==1:
          return 0
     elif n==2:
          return 1
     else:
          return fibonacci(n-1)+fibonacci(n-2)
     
n=int(input("enter n:"))
print(fibonacci(n))
#----print fibonacci sequence------
for i in range(1,n+1):
     print("fibonacci sequence:",fibonacci(i))

