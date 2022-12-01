print("Select 1 for (+), 2 for (-), 3 for (*) and 4 for (/)")

calculateAgain = 'yes'

while calculateAgain == 'yes':
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(num1, "+", num2, "=", (num1 + num2))

        elif choice == '2':
            print(num1, "-", num2, "=", (num1 - num2))

        elif choice == '3':
            print(num1, "*", num2, "=", (num1 * num2))

        elif choice == '4':
            print (num1, "/", num2, "=", (num1 / num2))
     
        # check if user wants another calculation
        # break the while loop if answer is no
        calculateAgain = input("Let's do next calculation? (yes/no): ")      
    else:
        print("Invalid Input")
    break