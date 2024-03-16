#  --------Python collections (Arrays)-------------
# 1. Lists
# 2. Tuple
# 3. Set
# 4. Dictionary

# -------Lists -----
# lists = [2,7,"akash",8.7,True]
# print(lists)
# print(type(lists))
# print(len(lists))
# if 7 in lists:
#      print("Present")
# else:
#      print("Not present")

# if "ak" not in lists:
#      print("not present")

# if "kash" in lists:
#      print("present")

# print(lists[1])
# print(lists[1:-1])

# #   ----append---------
# lists.append(65)
# print(lists)

# #    ----insert------
# lists.insert(2,"kumar")

#    -----extend-------
# list1 = [2,67,"abc",True,8.9]
# list2 = [4,89,62,"akg",True,False,6.8]
# list1.extend(list2)
# print(list1)

#     -----remove-------
# list2.remove(89)
# print(list2)

#     ------pop-removing element by index------
# list2.pop()           #if not provide index no., last element would remove by default
# print(list2)

# list2.pop(4)      # removing by index no.
# print(list2)

#     ---changing item in list-----
# fruits = ["apple","banana","pineapple","mango","guava"]
# print(fruits)
# fruits[1] = 45
# print(fruits)

# fruits[1:4]=["akash","kumar"]
# print(fruits)

#  ---sorting (ascending or descending) -----
# list = ["kash","akash","gupta"]
# list.sort()
# print(list)
# list.reverse()
# print(list)

# making descending in one line
# list = [23,67,45,90,67,12]
# list.sort(reverse=True)
# print(list)

#   ---------------list comprehension ---------
# make a new list having element greater than 50
# list = [45,67,34,28,89,56,61]
# new_list = [i for i in list if i>50]
# print(new_list)

# create a new list item having present "a"
# fruits = ["apple","mango","grapes","banana","cherry"]
# new_fruits = [fruits for fruits in fruits if "a" in fruits ]
# print(new_fruits)
# fr = new_fruits.copy()
# print(fr)

#    -------concatenate two lists ------------
# fruit1 = ["mango","grapes","apple","pineapple"]
# fruit2 = ["pineapple","guava"]
# fruits = fruit1 + fruit2
# print(fruit1+fruit2)

#    --------nested list----------
# list1 = [23,45,"akash",67.8,]
# list1.insert(2,["kumar",6.7])
# print(list1)
# print(list1[2])
# print(list1[2][1])

#     ----------swapping items in list---------
list = [23,65,19,90]         # interchange 23 and 19
# list[0] = 19
# list[2] = 23
# print(list)
#-----------------------
# n = int(input("Enter size of list:"))
# list = []
# for _ in range(n):
#      num = int(input())
#      list.append(num)

# idx1 = int(input("Enter here index 1: "))
# idx2 = int(input("Enter here index 2: "))
# print(list)
# temp = list[idx1]
# list[idx1] = list[idx2]
# list[idx2] = temp

# print(list)