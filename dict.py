birthdays = {'Joshi' : '14-12-2003', 'Obama' : '12-14-1987', 'Messi': '19-07-1980'}
print("We know the birthdays of ")

for x in birthdays:
    print('>> ', x)

user_choice = input("Who's birthday do you want to want to look up?: ")

if user_choice in birthdays:
    print("The birthday of ", user_choice , " is ", birthdays[user_choice])

else:
    print("We don't have {}'s birthday." .format(user_choice))


