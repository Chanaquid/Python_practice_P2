user_number = int(input('Type a number: '))
a = [x for x in range(2, user_number) if user_number % x == 0]

def prime_num(n):
    if user_number > 1:
        if len(a) == 0:
            print('It is a prime number')
        else:
            print('It is not a prime number')
    else:
        print('It is not a prime number')

prime_num(user_number)

#x = range(1, user_number + 1)
#divisors = []

#for num in x:
#    user_calculation =  user_number % num
#    if user_calculation == 0:
#        divisors.append(num)
#print(divisors)
