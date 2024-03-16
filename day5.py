# #     --------tuple---------
# tup = ("akash",67,8.9,"rt")
# print(type(tup))
# print(len(tup))
# print(tup[1])
# print(tup[1:3])
# print(tup[-2: ])

# #       ----------creating a tuple with one item----------
# # abc = tuple(("akash"))
# # print(abc)
# # print(type(abc))

# #          ----------item present in tuple or not---------
# if 67 in tup:
#      print("present")

# #       ------for traverse---------------
# for i in tup:
#      print(i)

     #    ---------concatenate two tuple-----------
# tup1 = ("akash","prakash",89,6.9)
# tup2 = ("sony",73,8.6)
# tup1 = tup1 + tup2
# print(tup1)

# #        =----------unpacking of tuple-----------
# tup = (67,"anshu",True)
# item1,item2,item3 = tup
# print(item1,item2,item3)

#     -----------reverse a tuple--------------
# tuple1 = ("sonam","ganga",67,8.9)          #tuple is immutable so not easy to reverse so use typecasting
# list = []

# for i in reversed(tuple1):
#      list.append(i)

# new_tuple = tuple(list)
# print(new_tuple)

#  ================ Sets ========================
# num = {1,2,3,4,5,6}
# print(type(num))
# print(len(num))
# print(num(1))                # find method to call sets item

#    --------check for item---------------------
# alphabet = {"a","c","r","o","u"}
# print(type(alphabet))
# if "c" in alphabet:
#      print("present")

#   --------add element in set-----------------
# alphabet = {"a","c","r","o","u"}
# alphabet.add("p")
# print(alphabet)

#   ---------add another sequence in set------------------
# list1 = ["akash","ria"]
# set1 = {45,"kia"}
# set1.update(list1)
# print(set1)

#  -----------removing item--------------
# alphabet = {"a","c","r","o","u"}
# alphabet.remove("r")
# print(alphabet)
# #    ===============
# alphabet.discard("z")      # no error if item not present
# print(alphabet)

# #  joining two set
# set1 = {"a","e","i","o"}
# set2 = {"a","apple","banana"}
# set3 = set1.union(set2)
# print(set3)
# # -----------or
# set1.update(set2)
# print(set1)

# #   -----------to print only duplicate value------------
# set1 = {"a","e","i","o"}
# set2 = {"a","apple","banana"}
# # set1.intersection_update(set2)
# # print(set1)
# #--------all values except duplicate---------
# set1.symmetric_difference_update(set2)
# print(set1)

# #   -------Question
# list1 = [1,5,10,20,40,80]
# list2 = [6,7,20,80,100]
# list3 = [3,4,15,20,30,70,80,120]

# list11 = set(list1)
# list22 = set(list2)
# list33 = set(list3)

# newlist = list11.intersection(list22)
# output = newlist.intersection(list33)
# print(output)

# #  ----------Dictionary--------------
# dict1 = {
#      "akash" : 2345,
#      "kumar" : 7865,
#      "gupta" : 5109
# }

# print(type(dict1))
# print(dict1["kumar"])
# print(dict1.get("akash"))
# print(dict1.keys())
# print(dict1.values())
# #    change key's value
# dict1["gupta"]=76554
# print(dict1)
# #    add new key value
# dict1["ok"]=123453
# print(dict1)

# dict2 = {
#      "ani":7851,
#      "all":6712
# }
# #  joining dict1 and dict2
# dict1.update(dict2)
# print(dict1)
# # remove element
# dict1.pop("ani")
# print(dict1)

# dict1.popitem()     #REMOVING last item
# print(dict1)
# #    empty the dictionary
# dict1.clear()
# print(dict1)

# printing values of a dictionary
# new_dict = {
#      "hello":"world",
#      "nice":"dress",
#      "okey":1234
#      }
# for x in new_dict:
#      print(x)
# for x in new_dict.items():
#      print(x)

# for x,y in new_dict.items():
#      print(x,y)

#    ---------nested dictionary---------
# new_dict = {
#      "hello":"world",
#      "nice":"dress",
#      "okey":1234,
#      "dict2":{
#           "apple":"sev",
#           "mango":"aam"
#      },
#      "dict3":{
#           "orange":"santra"
#      }
#      }
# #    print apple value
# print(new_dict["dict2"]["apple"])
# #  orange value
# print(new_dict["dict3"]["orange"])

#   ----------Question
# find valus sum
dict = {
     "asd":12,
     "aws":56,
     "azs":98,
     "nhg":56
}
print(sum(dict.values()))     
