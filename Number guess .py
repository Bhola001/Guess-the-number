print("=== We play a random guessing game ===")

import random

# Select a random number between 1 and 100
computer = random.randint(1, 100)

attempt = 0
while(True):
    you = int(input("Guess the number Between 1 to 100:"))
    attempt +=1

    if(you >=101 or you <=0):
        print(f"Plese Guess the number Between 1 to 100 🫵🏻")
    elif(computer < you):
        print(f"Please guess the Smaller number 📉")

    elif(computer > you):
        print(f"Please guess the Biger number 📈")
    
    else:  # computer == you
        print(f"🎉 Congratulations! You guessed the number in {attempt} attempts")

        break

    


