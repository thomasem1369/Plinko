# Plinko
# 25.2.26
# Emma Thomas

import random
import time

# Plinko Board
board = [[" ", "P", " ", "P", " ", "P", " ", "P", " "],
         ["P", " ", "P", " ", "P", " ", "P", " ", "P"],
         [" ", "P", " ", "P", " ", "P", " ", "P", " "],
         ["P", " ", "P", " ", "P", " ", "P", " ", "P"],
         [" ", "P", " ", "P", " ", "P", " ", "P", " "],
         ["P", " ", "P", " ", "P", " ", "P", " ", "P"]]

# Multipliers
slots = [5, 3, 1, 0.5, 0.2, 0.5, 1, 3, 5]


# Check is bet is a valid integer
while True:
    try:
        # Ask user how much money they would like to bet
        bet = float(input("Enter how much money you want to bet: $"))
        
        # Check for valid range
        if bet <= 0:
            print("Please enter a amount greater than $0.")
        else:
            print(f"Bet of ${bet} accepted.")
            break 
            
    except ValueError:
        # This catches non-numeric inputs (like letters)
        print("Invalid input. Please enter a numeric value.")

# Start from the middle of the board
column = len(board[0]) // 2

print("Dropping chip...")

# Simulate the chip falling through the board
for row in range(len(board)):

    if board[row][column] == "P":
        move = random.choice([-1, 1])
        new_column = column + move
        
        if 0 <= new_column < len(board[0]):
            column = new_column
     

    print("Chip at row", row, "column", column)
    time.sleep(1)

# Final multiplier
multiplier = slots[column]
winnings = bet * multiplier

print("\n--- RESULT ---")
print("Landed in slot", column)
print("Multiplier:", multiplier)
print("You won:${}".format(winnings))
