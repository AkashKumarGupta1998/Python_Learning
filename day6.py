#---------Mirror Operation question------------Timing 6:38 hrs
input_str = input("Enter string: ")
n = int(input("Enter n: "))

# first create dictionary of alphabets
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]
dict1 = dict(zip(alphabets,reverse_alphabets))
# finding string on which need to mirror operation
prefix = input_str[0:n-1]
suffix = input_str[n-1:]
# finding the mirror string
mirror = ""
for i in range(0,len(suffix)):
     mirror = mirror + dict1[suffix[i]]
#creating the final string
res = prefix + mirror
print("result is",res)