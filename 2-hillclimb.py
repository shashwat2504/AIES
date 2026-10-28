
def cost(path, graph):
    total = 0
    n = len(path)

    for i in range(n):
        total += graph[path[i]][path[(i + 1) % n]]

    return total


def hill_climbing(graph):
    n = len(graph)
    path = list(range(n))

    while True:
        best = path[:]

        for i in range(1, n):
            for j in range(i + 1, n):
                new = path[:]
                new[i], new[j] = new[j], new[i]

                if cost(new, graph) < cost(best, graph):
                    best = new

        if best == path:
            break

        path = best

    print("Best Path:", path + [path[0]])
    print("Minimum Cost:", cost(path, graph))


n = int(input("Enter number of cities: "))
graph = []

print("Enter Cost Matrix:")
for i in range(n):
    graph.append(list(map(int, input().split())))

hill_climbing(graph)





# # Function to calculate the total distance of a path
# def cost(path, graph):
#     total = 0                 # Store the total distance, initially zero
#     n = len(path)             # Count the number of cities in the path

#     for i in range(n):        # Visit each city position in the path
#         # Add distance from current city to the next city
#         # % n makes the last city connect back to the first city
#         total += graph[path[i]][path[(i + 1) % n]]

#     return total              # Return the complete tour distance


# # Function to solve TSP using Hill Climbing
# def hill_climbing(graph):
#     n = len(graph)            # Number of cities in the distance matrix
#     path = list(range(n))     # Create initial path: [0, 1, 2, ..., n-1]

#     while True:               # Repeat until no better path is found
#         best = path[:]        # Copy the current path as the best path

#         # Try swapping every possible pair of city positions
#         # Start from position 1 to keep the starting city fixed
#         for i in range(1, n):
#             for j in range(i + 1, n):
#                 new = path[:] # Copy the current path for testing

#                 # Swap two cities to create a neighboring path
#                 new[i], new[j] = new[j], new[i]

#                 # If the new path is shorter, save it as the best
#                 if cost(new, graph) < cost(best, graph):
#                     best = new

#         # If no better path was found, stop the algorithm
#         if best == path:
#             break

#         # Update the current path with the best path found
#         path = best

#     # Print the path and add the starting city at the end
#     print("Best Path:", path + [path[0]])

#     # Print the total distance of the final path
#     print("Minimum Cost:", cost(path, graph))


# # Take the number of cities as input and convert it to an integer
# n = int(input("Enter number of cities: "))

# # Create an empty list to store the distance matrix
# graph = []

# print("Enter Cost Matrix:")

# # Read each row of the distance matrix
# for i in range(n):
#     # Split the input, convert each value to an integer,
#     # create a list, and add that row to the matrix
#     graph.append(list(map(int, input().split())))

# # Call the function to find a shorter tour
# hill_climbing(graph)




# Enter number of cities: 4
# Enter Cost Matrix:
# 0 10 15 20
# 10 0 35 25
# 15 35 0 30
# 20 25 30 0


# Best Path: [0, 1, 3, 2, 0]
# Minimum Cost: 80