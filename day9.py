#-------Strings----------
# name1= 'akash'
# name2="kumar"
# name3='''gupta'''
# print(name1,name2,name3)
#----for multiline string
# information='''This is a 
# multiline string'''
# print(information)

#------array like indexing in strings------
# name="akash"
# print(name[1])
# print(name[-1])
# #------------traversing strings----------
# for i in name:
#      print(i)
#-----traverse by making list of strings-----------
# name="Prakash"
# name_list=list(name)
# print(name_list[0: ])
# #-----using list comprehension
# list=[char for char in name]
# for i in list:
#      print(i)

#------find a character---------
# name="constitution"
# print(name.find("ti"))
# print(name.find("aka"))

#--------Slicing a String--------------
# name="akashkumargupta"
# print(name[5: ])
# print(name[2:6])
# print(name[ :6])
# print(name[-2: ])

#----modifying string----------
#------converting character in upper case---------
# name="    bhim    rao    ambedkar     "
# name1=name.upper()
# print(name1)
# name2=name1.lower()
# print(name2)
# #-------for capitalizing of first character of string
# name3=name.capitalize()
# print(name3)
# #----for stripping/removing any trailing whitespaces-----
# print(name.strip())
# #-----replace
# print(name.replace("bhim","B"))   #replace all with "B"

# -----replace to a limit------
# statement="this is dog,this is cat,this is cow"
# print(statement.replace("this","that"))
# print(statement.replace("this","that",1))

#------splliting strings---------
# str1="abc,cgf,lkj,yhg,lig,cgy"
# list=str1.split()
# print(list)

# list1=str1.split(",,")
# print(list1)

# list2=str1.split(",",2)
# print(list2)

#---concatenate 
# str1="akash"
# str2="kumar"
# str3="gupta"
# all_str=str1+str2+str3
# print(all_str)

#----format() function in string---------
# student_name="akash"
# student_marks=96
# str1="The student name is {n}, and marks is {m}".format(n=student_name,m=student_marks)
# print(str1)

#----Escape character-------
#----------palindrome-original string=reversed string
def check_palindrome(str):
     clean_str=(str.replace(" ", "")).lower()

     reverse_str=clean_str[::-1]
     return clean_str==reverse_str

str=input("Enter a string: ")
if check_palindrome(str):
     print("It is a palindrome string")
else:
     print("Not a palindrome")