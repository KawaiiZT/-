import random
while True:
    choices = ["rock","paper","scrissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:    
        player = input("Rock,paper, or scissors?: ")
        print("compurt :",computer)
        print("player : ",player )
    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")
    elif player == "rock": 
        if computer == "paper":  
            print("computer: ",computer)
            print("player: ",player)
            print("you lose!")
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("you win!")
    elif player == "scisscors": 
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("you lose!")
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("you win!")
    elif player == "paper": 
        if computer == "scisscors":
            print("computer: ",computer)
            print("player: ",player)
            print("you lose!")
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("you win!")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!")