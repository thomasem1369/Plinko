# Plinko
# 25.2.26
# Emma Thomas

import random

# CONSTANTS
MAX_BET = 1000
ROWS = 12

# Multipliers for the bottom slots
slots = [5, 3, 1, 0.5, 0.2, 0.2, 0.5, 1, 3, 5, 3, 5]

def get_bet(balance):
    """
    Ask user how much money they would like to bet
    """
    while True:
        try:
            bet = float(input("Enter how much money you want to bet (you can not bet more than $1000): $"))
            # Check for valid range
            if bet <= 0:
                print("Please enter an amount greater than $0.")

            elif bet > MAX_BET:
                print("You cannot bet more than $1000.")

            elif bet > balance:
                print("You don't have that much money")

            else:
                print(f"Bet of ${bet} accepted.")
                return bet
        # This checks for non-numeric inputs like letters
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        

def simulate_path(total_rows):
    """
    Simulate the ball path and return list of column positions
    """

    column = 0
    path = []

    for row in range(total_rows):

        if row > 0:
            move = random.choice([0, 1])
            column += move

        path.append(column)
        
    return path, column

def draw_board(path, total_rows):
    """
    Print the plinko board
    """

    for row in range(total_rows):
        spaces = " " * (total_rows - row)
        line = spaces
        
        for column in range(row + 1):
            if column == path[row]:
                line += "● "
            else:
                line += "○ "

        print(line)

def calculate_payout(final_column, bet_amount):
    """
    Calculate winnings based on final column
    """

    multiplier = slots[final_column]
    winnings = bet_amount * multiplier
    
    return multiplier, winnings


def main():
    balance = 1000  # starting money
    playing = True

    while playing and balance > 0:

        print("\n--- NEW ROUND ---")
        
        bet = get_bet(balance)

        path, final_column = simulate_path(ROWS)
        draw_board(path, ROWS)

        multiplier, winnings = calculate_payout(final_column, bet)

        balance -= bet
        balance += winnings

        print("\n--- RESULT ---")
        print("Landed in slot:", final_column)
        print("Multiplier:", multiplier)
        print("You won: ${:.2f}".format(winnings))
        print("New balance: ${:.2f}".format(balance))

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


# Run the game
main()




