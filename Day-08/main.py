#Reversing a string

name = "ASA"
list = list(name)
rev_name = ""
for i in range(len(list),0,-1):
    rev_name  += list[i-1]

print(rev_name)
print(name)
if rev_name == name:
    print("It's a palindrome")



