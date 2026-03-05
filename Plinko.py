# Plinko
# 25.2.26
# Emma Thomas

import random

rows = 12

# Multipliers for the bottom slots
slots = [5, 3, 1, 0.5, 0.2, 0.2, 0.5, 1, 3, 5, 3, 5]

# Ask user how much money they would like to bet
while True:
    try:
        bet = float(input("Enter how much money you want to bet (you can not bet more than $1000): $"))
        # Check for valid range
        if bet <= 0:
            print("Please enter an amount greater than $0.")

        elif bet > 1000:
            print("You cannot bet more than $1000.")

        else:
            print(f"Bet of ${bet} accepted.")
            break
    # This checks for non-numeric inputs like letters
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

playing = True

while playing:

    column = 0
    path = []

    # Simulate ball path
    for row in range(rows):

        if row > 0:
            move = random.choice([0, 1])
            column += move

        path.append(column)

    # Print plinko board
    for r in range(rows):

        spaces = " " * (rows - r)
        line = spaces

        for c in range(r + 1):

            if path[r] == c:
                line += "● "
            else:
                line += "○ "

        print(line)

    # Calculate winnings
    final_column = path[-1]
    multiplier = slots[final_column]
    winnings = bet * multiplier

    # Print the final results
    print("\n--- RESULT ---")
    print("Landed in slot", column)
    print("Multiplier:", multiplier)
    print("You won: ${}".format(winnings))

    # Ask user if they would like to continue playing
    while True:
        again = input("Would you like to continue playing? (y/n): ").strip().lower()

        if again == "y":
            bet = winnings
            print("This round bet: $", bet)
            break

        elif again == "n":
            print("Thank you for playing!")
            playing = False
            break

        else:
            print("Invalid input. Please enter 'y' or 'n'.")

