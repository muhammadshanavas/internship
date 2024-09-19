import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        # Prompt the user to make a choice
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        # Ensure user enters a valid choice
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, please choose rock, paper, or scissors.")
            continue

        # Computer makes a random choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Display both choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)

        # Update and display the result
        if result == "tie":
            print("It's a tie!\n")
        elif result == "user":
            print("You win this round!\n")
            user_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1

        # Display the current scores
        print(f"Scores: You {user_score} - {computer_score} Computer\n")

        # Ask the user if they want to play again
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nFinal Scores:")
            print(f"You: {user_score} - Computer: {computer_score}")
            print("Thanks for playing!")
            break

# Call the play_game function to start the game
play_game()
