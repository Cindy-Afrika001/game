import random

user = 0
computer = 0

options = ("rock","paper","scissors")

while True:
    user_input = input("Type Rock/Paper/scissors or q to quit: ").lower()
    if user_input == "q":
        break
        
random_number = random.randint(0,2)
computer_pick =options[random_number]
print("computer picked",computer_pick + ".")
if user == "rock" & computer == "scissors":
    print("Congrats honey")
    user += 1

elif  user == "paper" & computer == "rock": 
     print("excellent")
     user += 1

elif user == "scissors" & computer == "paper":
   print("winner winner!!")
   user += 1

else:
    print("try next time!!")
    computer += 1

print("You won", user, "times.")
print("Robot did it", computer, "times.")
print("Goodbye chommy!")
