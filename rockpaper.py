import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("Type 'rock', 'paper', or 'scissors'. Type 'exit' to quit.\n")

    while True:
        user_choice = input("Your move: ").lower()

        if user_choice == 'exit':
            print("Thanks for playing!")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            user_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!")

        print(f"Score — You: {user_score} | Computer: {computer_score}\n")

if __name__ == "__main__":
    play_game()