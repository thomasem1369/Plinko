# Plinko
# 25.2.26
# Emma Thomas

import random

# CONSTANTS
ROWS = 12
START_BALANCE = 1000
WHALE_THRESHOLD = 500

# Multipliers for the bottom slots
slots = [5, 3, 1, 0.5, 0.2, 0.2, 0.5, 1, 3, 5, 3, 5]


def create_player_profile():
    """Asks user for information to create and return their profile."""
    # Get user name and location
    name = input("Enter name: ")
    location = input("Enter location: ")

    # Stores user data
    return {
        "name": name,
        "location": location,
        "high_score": 0,
        "lifetime_losses": 0,
        "target_ads": False
    }


def get_bet(balance):
    """Ask user how much money they would like to bet."""
    bet = float(input(f"Enter how much to bet (max ${balance:.2f}): $"))
    while True:
        try:
            # Check for valid range (higher than 0)
            if bet <= 0:
                print("Please enter an amount greater than $0.")

            # If bet is higher tha ntheir avalable balance:
            elif bet > balance:
                print("You cannot bet more than your current balance.")

            # When bet is valid:
            else:
                print(f"Bet of ${bet:.2f} accepted.")
                return bet

        # This checks for non-numeric inputs like letters
        except ValueError:
            print("Invalid input. Please enter a numeric value.")



def simulate_path(total_rows):
    """Simulate the ball path and return list of column positions."""
    column = 0
    path = []

    # Random generator for ball path
    for row in range(total_rows):

        if row > 0:
            move = random.choice([0, 1])
            column += move

        path.append(column)

    return path, column


def draw_board(path, total_rows):
    """Print the plinko board."""
    # Creates plinko board
    for row in range(total_rows):
        spaces = " " * (total_rows - row)
        line = spaces

        # "● " is the ball and "○ " are the pins for each row
        for column in range(row + 1):
            if column == path[row]:
                line += "● "

            else:
                line += "○ "

        print(line)


def calculate_payout(final_column, bet_amount):
    """Calculate and return multiplier and winnings based on final column."""
    multiplier = slots[final_column]    # Retrieves multiplier
    winnings = bet_amount * multiplier  # Calculates amount won

    return multiplier, winnings


def check_marketing_status(player_profile):
    """Check if player is a 'whale'."""
    # Prints ad when player is eligible
    if player_profile["lifetime_losses"] > WHALE_THRESHOLD:
        print("VIP OFFER: Double your next deposit! Buy more credits now!")
        player_profile["target_ads"] = True
    else:
        print("Keep playing to climb the leaderboard!")


# Main routine
def main():
    """Run the main part of the game."""
    player_profile = create_player_profile()
    balance = START_BALANCE  # Starting money
    playing = True

    while playing and balance > 0:

        # Opening screen for each round
        print("\n--- NEW ROUND ---")
        print(f"Player: {player_profile['name']} ({player_profile['location']})")
        print(f"Balance: ${balance:.2f}")

        bet = get_bet(balance)

        path, final_column = simulate_path(ROWS)
        draw_board(path, ROWS)

        multiplier, winnings = calculate_payout(final_column, bet)

        balance -= bet
        balance += winnings

        # Loss tracking
        if winnings < bet:
            loss = bet - winnings
            player_profile["lifetime_losses"] += loss

        # High scpre update
        if balance > player_profile["high_score"]:
            player_profile["high_score"] = balance

        print("\n--- RESULT ---")
        print("Landed in slot:", final_column)
        print("Multiplier:", multiplier)
        print("You won: ${:.2f}".format(winnings))
        print("New balance: ${:.2f}".format(balance))

        # Marketing check
        check_marketing_status(player_profile)

        if balance < 1:
            print("/n You do not have enough money to continue.")
            break

        # Asks if user would like to play again
        while True:
            again = input("Play again? (y/n): ").strip().lower()
            if again == "y":
                break
            elif again == "n":
                playing = False
                print("Thanks for playing!")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    # Final stats screen
    profit = balance - START_BALANCE

    print("\n--- GAME OVER ---")
    print(f"High score: ${player_profile['high_score']:.2f}")
    print(f"Lifetime losses: ${player_profile['lifetime_losses']:.2f}")
    print(f"Target ads enabled: {player_profile['target_ads']}")

    # Checks user profits
    if profit > 0:
        print("You made a profit of ${:.2f}".format(profit))
    elif profit < 0:
        # Absolute value returns positive integer for printing
        print("You lost ${:.2f}".format(abs(profit)))
    else:
        print("You broke even.")


# Call the game
if __name__ == "__main__":
    main()
