# Lets Make A Rock - Paper - Scissors Game
# Author : tousifnehal

#importing modules
import random

# Computer Choosing Function
computer = None

random_val = random.randint(1,3)

if random_val == 1:
    computer = "r"
elif random_val == 2:
    computer = "p"
elif random_val == 3:
    computer = "s"  
    
# User Choosing Options
user = input("""What Do You Choose \n Type :- \n \tr for choosing rock 🧱 \n \tp for choosing paper 📜 \n \ts for choosing scissors ✂ \n""")

# RPS Game Function  
    
def game(computer , user):
    print("The Computer is choosing.....")   
    if computer == user == "r" :
        print(f"The Computer & You Both Choose Rock 🧱 & it was a tie ➖")
    elif computer == user == "p" :
        print(f"The Computer & You Both Choose Paper 📜 & it was a tie ➖")
    elif computer == user == "s" :
        print(f"The Computer & You Both Choose Scissors ✂  & it was a tie ➖")
        #Rock For Computer :
    if computer == "r":
        if user == "s" :
            print(f"Computer Choose Rock 🧱 & You Choose Scissors ✂, You Lost ❌ ")
        elif user == "p" :
            print(f"Computer Choose Rock 🧱 & You Choose Paper 📜, You Win ✅ ")
    elif computer == "p":
        if user == "s":
            print(f"Computer Choose Paper 📜 & You Choose Scissors ✂, You Win ✅")
        elif user == "r" :
            print(f"Computer Choose Paper 📜 & You Choose Rock 🧱, You Lost ❌ ")
    elif computer == "s":
        if user == "p":
            print(f"Computer Choose Scissors ✂ & You Choose Paper 📜, You lost ❌ ")
        elif user == "r" :
            print(f"Computer Choose Scissors ✂ & You Choose Rock 🧱, You win ✅")
  
# Calling The Function          

game(computer, user)