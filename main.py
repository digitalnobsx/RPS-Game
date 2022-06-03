import random

while True:
    options = ["R", "P", "S"]

    print("Starting Game \nThis is a Rock, Paper, Scissors game")

    computer = random.choice(options)
    player = None


    player = input("Type 'R' for 'Rock', 'P' for 'Paper', and 'S' for 'Scissors': ").upper()

    for letter in player:
        if letter in options:
            continue
    else:
        print("Invalid Input. Please input R, P, or S: ")
    
    if player == computer:
        print("CPU (",computer + ") : ", end = ' ')
        print("player (",player +")")
        print("Tie!")
        continue
    elif player == "R":
        if computer == "P":
            print("CPU (",computer + ") : ", end = ' ')
            print("player (",player +")")
            print("You Lose!")
            break
        if computer == "S":
            print("CPU (",computer + ") : ", end = ' ')
            print("player (",player +")")
            print("You Win!")
            break

    elif player == "S":
        if computer == "P":
            print("CPU (",computer + ") : ", end = ' ')
            print("player (",player +")")
            print("You Win!")
            break
        if computer == "R":
            print("CPU (",computer + ") : ", end = ' ')
            print("player (",player +")")
            print("You Lose!")
            break
    elif player == "P":
        if computer == "S":
            print("CPU (",computer + ") : ", end = ' ')
            print("player (",player +")")
            print("You Lose!")
            break
        if computer == "R":
            print("CPU (",computer + ") : ", end = ' ')
            print("player (",player +")")
            print("You Win! ")
            break
