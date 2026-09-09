import random
# GAME RULES
def determine_winner(player, computer):

    if player == computer:
        return "tie"

    winning_combinations = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if winning_combinations[player] == computer:
        return "player"

    return "computer"

# DISPLAY SCORES

def display_score(player_score, computer_score, ties):

    print("                    SCOREBOARD")
    print(f"Player Score   : {player_score}")
    print(f"Computer Score : {computer_score}")
    print(f"Ties           : {ties}")

# GET PLAYER CHOICEy
def get_player_choice():

    while True:

        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("Enter your choice: ").strip()

        choices = {
            "1": "rock",
            "2": "paper",
            "3": "scissors"
        }

        if choice in choices:
            return choices[choice]

        print("Invalid choice. Please select 1, 2, or 3.")


def play_round():

    player_choice = get_player_choice()

    options = ["rock", "paper", "scissors"]

    computer_choice = random.choice(options)

    print("\n" + "-" * 50)
    print(f"Your Choice      : {player_choice.upper()}")
    print(f"Computer Choice  : {computer_choice.upper()}")
    print("-" * 50)

    result = determine_winner(
        player_choice,
        computer_choice
    )

    if result == "player":
        print("🎉 You Win!")

    elif result == "computer":
        print("💻 Computer Wins!")

    else:
        print("🤝 It's a Tie!")

    return result

# MAIN GAME
def main():

    player_score = 0
    computer_score = 0
    ties = 0

    print("\n" + "=" * 60)
    print("             ROCK - PAPER - SCISSORS")
    print("=" * 60)

    print("\nGame Rules:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")

    while True:

        result = play_round()

        if result == "player":
            player_score += 1

        elif result == "computer":
            computer_score += 1

        else:
            ties += 1

        display_score(
            player_score,
            computer_score,
            ties
        )

        again = input(
            "\nDo you want to play another round? (Y/N): "
        ).strip().lower()

        if again not in ["y", "yes"]:
            break

    print("\n" + "=" * 60)
    print("                   FINAL RESULT")
    print("=" * 60)

    display_score(
        player_score,
        computer_score,
        ties
    )

    if player_score > computer_score:
        print("🏆 Congratulations! You are the overall winner!")

    elif computer_score > player_score:
        print("💻 Computer wins the game!")

    else:
        print("🤝 The game ended in a draw!")

    print("\nThank you for playing!")


if __name__ == "__main__":
    main()