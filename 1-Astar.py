from queue import PriorityQueue

def read():
    return [list(map(int, input().split())) for i in range(3)]


def h(s, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != 0 and s[i][j] != goal[i][j]:
                count += 1
    return count


def astar(start, goal):
    pq = PriorityQueue()
    pq.put((h(start, goal), 0, start))
    visited = []

    while not pq.empty():
        f, g, s = pq.get()

        if s in visited:
            continue
        visited.append(s)

        print("Visited State:")
        for row in s:
            print(row)
        print("f =", f, "g =", g, "h =", h(s, goal))
        print()

        if s == goal:
            print("Goal Reached!")
            return

        x, y = 0, 0
        for i in range(3):
            for j in range(3):
                if s[i][j] == 0:
                    x, y = i, j

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new = [row[:] for row in s]

                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]

                if new not in visited:
                    ng = g + 1
                    nh = h(new, goal)
                    pq.put((ng + nh, ng, new))

    print("No Solution Found")


print("Enter Initial State (0 = Blank):")
start = read()

print("Enter Goal State:")
goal = read()

astar(start, goal)








    # Import PriorityQueue to process states according to their priority
from queue import PriorityQueue


# Function to read a 3x3 puzzle from the user
def read():
    # Read 3 rows, convert each number to an integer, and store them in a list
    return [list(map(int, input().split())) for i in range(3)]


# Heuristic function: counts the number of misplaced tiles
def h(s, goal):
    count = 0  # Initially, no tiles are misplaced

    # Visit every row and column of the puzzle
    for i in range(3):
        for j in range(3):

            # Ignore 0 because it represents the blank space
            # Count a tile if it is not in its correct position
            if s[i][j] != 0 and s[i][j] != goal[i][j]:
                count += 1

    # Return the total number of misplaced tiles
    return count


# A* search algorithm to solve the 8-puzzle
def astar(start, goal):

    # Create a priority queue to store states according to their f-value
    pq = PriorityQueue()

    # Add the initial state to the queue
    # f = g + h, where g = 0 and h = estimated remaining cost
    pq.put((h(start, goal), 0, start))

    # Store states that have already been explored
    visited = []

    # Continue searching while the priority queue is not empty
    while not pq.empty():

        # Remove the state with the lowest priority value
        # f = estimated total cost, g = cost so far, s = current state
        f, g, s = pq.get()

        # If this state has already been explored, skip it
        if s in visited:
            continue

        # Mark the current state as visited
        visited.append(s)

        # Display the state currently being explored
        print("Visited State:")

        # Print each row of the puzzle
        for row in s:
            print(row)

        # Display the f, g, and h values of this state
        print("f =", f, "g =", g, "h =", h(s, goal))
        print()

        # Check whether the current state matches the goal state
        if s == goal:
            print("Goal Reached!")
            return  # Stop the algorithm because the goal is found

        # Initialize the blank tile's position
        x, y = 0, 0

        # Search the current state for the blank tile, represented by 0
        for i in range(3):
            for j in range(3):
                if s[i][j] == 0:
                    x, y = i, j  # Save its row and column

        # Possible movements of the blank tile:
        # (-1, 0) = up, (1, 0) = down
        # (0, -1) = left, (0, 1) = right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Try each possible movement
        for dx, dy in moves:

            # Calculate the blank tile's new position
            nx = x + dx
            ny = y + dy

            # Check that the new position is inside the 3x3 puzzle
            if 0 <= nx < 3 and 0 <= ny < 3:

                # Create a copy of the current state
                # This prevents changes to the original state
                new = [row[:] for row in s]

                # Swap the blank tile with the adjacent tile
                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]

                # Only add the new state if it has not been explored
                if new not in visited:

                    # Increase the path cost by 1 for this move
                    ng = g + 1

                    # Calculate the heuristic for the new state
                    nh = h(new, goal)

                    # Calculate f = g + h and add the new state to the queue
                    pq.put((ng + nh, ng, new))

    # Execute this if the queue becomes empty without finding the goal
    print("No Solution Found")


# ---------------- MAIN PROGRAM ----------------

# Ask the user to enter the initial puzzle state
print("Enter Initial State (0 = Blank):")

# Read and store the initial state
start = read()

# Ask the user to enter the desired goal state
print("Enter Goal State:")

# Read and store the goal state
goal = read()

# Run the A* algorithm using the initial and goal states
astar(start, goal)