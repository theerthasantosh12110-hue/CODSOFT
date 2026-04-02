import random

while True:
    u=input("Enter choice (rock/paper/scissors):")
    print("You chose:",u)

    c=["rock","paper","scissors"]
    comp=random.choice(c)
    print("Computer chose:",comp)

    if u=="rock" and comp=="scissors":
        print("You win!")
    elif u=="scissors" and comp=="paper":
        print("You win!")
    elif u=="paper" and comp=="rock":
        print("You win!")
    elif u==comp:
        print("Tie")
    else:
        print("You lose!")
        print("Better luck next time!")
    
    again=input("Do you want to play again?").lower()
    if again=="no":
        print("Game over")
        break