import random


class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.max_score = 3

    def validate_choice(self, choice):
        return choice in self.choices

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "scissors" and computer_choice == "paper") or
            (player_choice == "paper" and computer_choice == "rock")
        ):
            self.player_score += 1
            return "player"
        else:
            self.computer_score += 1
            return "computer"

    def check_winner(self):
        if self.player_score >= self.max_score:
            return "player"
        elif self.computer_score >= self.max_score:
            return "computer"
        return None


if __name__ == "__main__":
    game = RockPaperScissors()

    while True:
        player_choice = input("Enter rock, paper or scissors: ").lower()

        if not game.validate_choice(player_choice):
            print("Invalid choice!")
            continue

        computer_choice = game.get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = game.determine_winner(player_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        else:
            print(f"{winner.capitalize()} wins this round")

        overall_winner = game.check_winner()
        if overall_winner:
            print(f"{overall_winner.capitalize()} wins the game!")
            break

        print(
            f"Score: Player {game.player_score} - Computer {game.computer_score}"
        )
