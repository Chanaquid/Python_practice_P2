## LIST OVERLAP

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

##version 1
for i in set(a):
    if i in b:
        c.append(i)
print(c)

##version 2
print(list(set(a)& set(b)))

#version 3
for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)

# version 4
print(list(x for x in set(a) if x in b))


## LIST COMPREHENSION
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if x % 2 == 0]
print(b)
"""

## LIST OVERLAP COMPREHENSION
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [i for i in set(a) if i in b]
print(c)
"""

## LIST ENDS
"""
a =[5, 10, 15, 20, 25]
def list_ends(a_list):
    return [a[0], a[-1]]
print(list_ends(a))
"""

## STRING LISTS
"""
user_input = input("Enter your text here:").lower()
if user_input == user_input[::-1]:
    print("This is a Palindrome text")
else:
    print("This is not a Palindrome text")
"""

## LIST REMOVE DUPLICATES
"""
a = [1, 2, 3, 4, 5, 5, 1, 2, 4, 4, 6, 7, 6, 8, 9, 10, 10]
def rmv_dupli(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

def rmv_dupli2(x):
    return list(set(x))

print(a)
print(rmv_dupli(a))
print(rmv_dupli2(a))
"""