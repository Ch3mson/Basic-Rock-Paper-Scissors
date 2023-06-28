import random

choice = int(input("1. Rock 2. Paper 3. Scissor 4. End the game"))

compChoice = random.randrange(3)+1
print(compChoice)

if compChoice == 1:
    print("The computer chose rock!")
    if choice == 1:
        print("Tie")
    elif choice == 2:
        print("Win!")
    elif choice == 3:
        print("You lose...")

if compChoice == 2:
    print("The computer chose paper!")
    if choice == 1:
        print("You lose...")
    elif choice == 2:
        print("Tie!")
    elif choice == 3:
        print("Win!")

if compChoice == 3:
    print("The computer chose scissors!")
    if choice == 1:
        print("Win!")
    elif choice == 2:
        print("You lose...!")
    elif choice == 3:
        print("Tie")

