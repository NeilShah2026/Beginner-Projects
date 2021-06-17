# Rock Paper Scissors
import random

options = ['Rock', 'Paper', 'Scissors']

x = 1
for i in options:
    print(f"{x}. " + i)
    x = x + 1

question = int(input("Enter Your Move: "))

computer = random.choice(options)
print(computer)
def pick(number):

    if number == 1:
        return "Rock"

    elif number == 2:
        return "Paper"

    elif number == 3:
        return "Scissors"

user_move = pick(question)

if user_move == computer:
    print("Tie!")

elif user_move == "Rock" and computer == "Paper":
    print("Hey, I Won!")

elif user_move == "Paper" and computer == "Rock":
    print("Hey, You Won!")

elif user_move == "Rock" and computer == "Scissors":
    print("Ayy, You Won!")

elif user_move == "Scissors" and computer == "Rock":
    print("Lez Go, I Won!")

elif user_move == "Paper" and computer == "Scissors":
    print("I Won!!!")

elif user_move == "Scissors" and computer == "Paper":
    print("You Won!!!")
