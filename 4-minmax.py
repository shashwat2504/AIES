b = [" "] * 9

def display():
    for i in range(0, 9, 3):
        print(b[i], "|", b[i+1], "|", b[i+2])
        if i < 6:
            print("---------")

def win(p):
    lines = [(0,1,2), (3,4,5), (6,7,8),
             (0,3,6), (1,4,7), (2,5,8),
             (0,4,8), (2,4,6)]

    for a, c, d in lines:
        if b[a] == b[c] == b[d] == p:
            return True
    return False

def minimax(p):
    if win("O"): return 1
    if win("X"): return -1
    if " " not in b: return 0

    best = -2 if p == "O" else 2

    for i in range(9):
        if b[i] == " ":
            b[i] = p
            next_p = "X" if p == "O" else "O"
            score = minimax(next_p)
            b[i] = " "

            if p == "O":
                best = max(best, score)
            else:
                best = min(best, score)

    return best

while True:
    display()
    m = int(input("Your move (1-9): ")) - 1

    if m < 0 or m > 8 or b[m] != " ":
        print("Invalid move")
        continue

    b[m] = "X"

    if win("X"):
        display()
        print("You win!")
        break

    if " " not in b:
        display()
        print("Draw!")
        break

    best, move = -2, -1

    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            score = minimax("X")
            b[i] = " "

            if score > best:
                best, move = score, i

    b[move] = "O"

    if win("O"):
        display()
        print("Computer wins!")
        break

    if " " not in b:
        display()
        print("Draw!")
        break










# Create a board with 9 empty cells
b = [" "] * 9


# Function to display the Tic-Tac-Toe board
def display():
    # Visit the starting index of each row: 0, 3 and 6
    for i in range(0, 9, 3):
        # Print the three cells of the current row
        print(b[i], "|", b[i+1], "|", b[i+2])

        # Print a horizontal line after the first two rows
        if i < 6:
            print("---------")


# Function to check whether player p has won
def win(p):
    # Store all 8 winning combinations:
    # 3 rows, 3 columns and 2 diagonals
    lines = [(0,1,2), (3,4,5), (6,7,8),
             (0,3,6), (1,4,7), (2,5,8),
             (0,4,8), (2,4,6)]

    # Check each winning combination
    for a, c, d in lines:
        # If all 3 cells contain the same player's symbol
        if b[a] == b[c] == b[d] == p:
            return True  # The player has won

    return False  # No winning combination was found


# Minimax predicts the result of future moves
def minimax(p):
    # If O wins, return +1 because O wants to win
    if win("O"): return 1

    # If X wins, return -1 because O wants to avoid losing
    if win("X"): return -1

    # If the board is full and nobody wins, return 0 for draw
    if " " not in b: return 0

    # O maximizes the score, so start below all scores
    # X minimizes the score, so start above all scores
    best = -2 if p == "O" else 2

    # Try every position on the board
    for i in range(9):

        # Only consider empty cells
        if b[i] == " ":

            # Temporarily place the current player's symbol
            b[i] = p

            # Switch to the other player's turn
            next_p = "X" if p == "O" else "O"

            # Recursively calculate the score of this move
            score = minimax(next_p)

            # Undo the temporary move to try another possibility
            b[i] = " "

            # O chooses the highest score
            if p == "O":
                best = max(best, score)

            # X chooses the lowest score
            else:
                best = min(best, score)

    # Return the best score found for the current player
    return best


# Keep playing until someone wins or the game is drawn
while True:

    # Display the current board
    display()

    # Ask the human to enter a position from 1 to 9
    # Subtract 1 because Python indexes start from 0
    m = int(input("Your move (1-9): ")) - 1

    # Reject positions outside the board or already occupied
    if m < 0 or m > 8 or b[m] != " ":
        print("Invalid move")
        continue  # Ask the human to enter another position

    # Place the human player's symbol X
    b[m] = "X"

    # Check whether the human has won
    if win("X"):
        display()
        print("You win!")
        break  # End the game

    # If no empty cells remain, the game is a draw
    if " " not in b:
        display()
        print("Draw!")
        break

    # Initialize the best score and best move for computer O
    best, move = -2, -1

    # Try every position to find the best computer move
    for i in range(9):

        # Consider only empty cells
        if b[i] == " ":

            # Temporarily place O in this cell
            b[i] = "O"

            # Evaluate this move using Minimax
            # X will play next in the simulated game
            score = minimax("X")

            # Remove the temporary O after evaluation
            b[i] = " "

            # If this move has a higher score, save it
            if score > best:
                best, move = score, i

    # Place O permanently at the selected best position
    b[move] = "O"

    # Check whether the computer has won
    if win("O"):
        display()
        print("Computer wins!")
        break  # End the game

    # Check whether the board is full after the computer's move
    if " " not in b:
        display()
        print("Draw!")
        break  # End the game
