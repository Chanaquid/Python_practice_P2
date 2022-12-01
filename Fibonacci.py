#user_input = int(input("Enter the number of Fibonacci numbers to generate: "))
def fibon_gen():
    count = int(input("Enter the number of Fibonacci numbers to generate: "))
    i = 1

    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count -1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibon_gen())
