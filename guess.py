import random as rand
comp_num = rand.randint(1,9)
user_guess = 0
tries = 0

while user_guess != comp_num and user_guess != "exit":
    user_guess = input("Guess a number: ")  

    if user_guess == "exit":
        break
    user_guess = int(user_guess)
    tries += 1

    if comp_num > user_guess:
        print("too low")

    elif comp_num < user_guess:
        print("too high")
    
    else:
        print("Exactly Right!!!")
        print("You only took ",tries, " tries!")
input()