import random

def play_rps():
    print("Welcome to Rock, Paper, Scissors!")
    player_name = input("Enter your name: ")
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input(f"{player_name}, enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer's choice: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print(f"{player_name} wins! Rock beats scissors.")
            else:
                print("Computer wins! Paper beats rock.")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print(f"{player_name} wins! Paper beats rock.")
            else:
                print("Computer wins! Scissors beats paper.")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print(f"{player_name} wins! Scissors beats paper.")
            else:
                print("Computer wins! Rock beats scissors.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_rps()
