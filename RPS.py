import random

def play_rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return

    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")

play_rock_paper_scissors()
