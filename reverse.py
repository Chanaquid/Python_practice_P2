user_inputs = input("Enter a sentence here: ")
reversed_inputs = user_inputs.split()[::-1]
reversed_lst = []
for i in reversed_inputs:
    reversed_lst.append(i)
print(" ".join(reversed_lst))
