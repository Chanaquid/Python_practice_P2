import random
import time

roll_again = "y"

while roll_again == "y":
    
    print("Rolling the dice:")
    time.sleep(2)
    print("The values are:", random.randint(1,6))
    roll_again = input("Roll again (y/n): ")
    

