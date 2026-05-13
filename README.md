🎯 Number Guessing Game
A simple and fun Python game where the computer randomly selects a number between 1 and 100, and the player tries to guess it.

🚀 Features


Random number generation using Python


Unlimited guessing attempts


Hints for:


Bigger number 📈


Smaller number 📉




Attempt counter


Input validation for numbers between 1 to 100



🛠️ Technologies Used


Python 3


random module



📂 Project Structure
📁 Number-Guessing-Game ┣ 📄 game.py ┗ 📄 README.md

▶️ How to Run


Install Python on your computer.


Clone this repository:


git clone https://github.com/your-username/Number-Guessing-Game.git


Open the project folder:


cd Number-Guessing-Game


Run the game:


python game.py

💻 Game Code

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

🎮 Example Output

Guess the number Between 1 to 100: 50
Please guess the Bigger number 📈

Guess the number Between 1 to 100: 75
Please guess the Smaller number 📉

Guess the number Between 1 to 100: 63
🎉 Congratulations! You guessed the number in 3 attempts

🌟 Future Improvements


Difficulty levels (Easy, Medium, Hard)


Limited attempts mode


GUI version using Tkinter


Score system


Multiplayer mode



👨‍💻 Author
Made with ❤️ by Bhola kumar

📜 License
This project is open-source and free to use.
