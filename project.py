from random import shuffle
from random import randint
import time

#Random Maze Generator and Solver
#Main function of the program
def main():
    choose_an_algorithm()

#Acts as the menu of the program
def choose_an_algorithm():
    height, width = get_width_height()

    while True:
        try:
            print("1. Run the depth first search algorithm.")
            print("2. Run the direct search algorithm.")
            print("3. Run both and compare their times.")
            print("4. Exit")
            option = int(input("Choose an option: "))

            if option == 1:
                maze, finish, start = create_maze(height, width)
                start_time = time.time()
                depth_first_search(maze, 1 , 1, height, width, finish)
                print("The result of depth first search algorithm: ")
                for row in maze:
                    print("".join(row))
                print("--- Depth First Search Time: %s seconds ---" % (time.time() - start_time))


            elif option == 2:
                maze, finish, start = create_maze(height, width)
                start_time = time.time()
                direct_path(maze, start, finish)
                print("The result of direct search algorithm: ")
                for row in maze:
                    print("".join(row))
                print("--- Direct Path Time: %s seconds ---" % (time.time() - start_time))

            elif option == 3:
                maze, finish, start = create_maze(height, width)
                depth_time = time.time()
                depth_first_search(maze, 1 , 1, height, width, finish)
                print("The result of depth first search algorithm: ")
                for row in maze:
                    print("".join(row))
                print("------------------------------")


                direct_time = time.time()
                direct_path(maze, start, finish)
                print("The result of direct search algorithm: ")
                for row in maze:
                    print("".join(row))


                print("--- Depth First Search Time: %s seconds ---" % (time.time() - depth_time))
                print("--- Direct Path Time: %s seconds ---" % (time.time() - direct_time))

            elif option == 4:
                break

            else:
                print("Invalid option")

        except (ValueError, TypeError):
            print("Provide a number.")


#Asks the user to input the width and the height, makes sure the values are odd for better algorithm use, returns the values
def get_width_height():
    while True:
        try:
            h = int(input("Height: "))
            if h > 0:
                break
            else:
                print("Please provide a positive number.")
        except (ValueError, TypeError):
            print("Provide a number.")

    while True:
        try:
            w = int(input("Width: "))
            if w > 0:
                break
            else:
                print("Please provide a positive number.")
        except (ValueError, TypeError):
            print("Provide a number.")

    if h % 2 == 0:
        h += 1

    if w % 2 == 0:
        w += 1
    print(f"The maze height will be {h} and the width will be {w}")
    return h, w

#Initializes a 2D array based on the height and width values, which we use as our maze
def create_maze(h, w):
    maze = [["#" for _ in range(w)] for _ in range(h)]

    # Ensure start and finish are not placed on the wall
    while True:
        start = (randint(1, h - 2), randint(1, w - 2))  # Random position inside the maze
        if maze[start[0]][start[1]] == "#":
            break

    while True:
        finish = (randint(1, h - 2), randint(1, w - 2))  # Random position inside the maze
        if maze[finish[0]][finish[1]] == "#" and finish != start:
            break

    # Place S and F in the maze
    maze[start[0]][start[1]] = "S"
    maze[finish[0]][finish[1]] = "F"
    return maze, start, finish

#Carves paths through the maze using depth first search and recursive backtracking
def depth_first_search(maze, x, y, h, w, finish):
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

    #Randomly shuffles the directions
    shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if (nx, ny) == finish:
            maze[x + dx // 2][y + dy // 2] = "."
            return

        if 0 < nx < h - 1 and 0 < ny < w - 1 and maze[nx][ny] == "#":
            maze[x + dx // 2][y + dy // 2] = "."
            maze[nx][ny] = "."
            depth_first_search(maze, nx, ny, h, w, finish)

# Carves a direct path from start to finish
def direct_path(maze, start, finish):
    x, y = start
    fx, fy = finish

    maze[x][y] = "S"
    maze[fx][fy] = "F"

    if x < fx:
        for i in range(x + 1, fx + 1):
            if maze[i][y] != "F": #Makes sure F doesn't get replaced
                maze[i][y] = "."
    elif x > fx:
        for i in range(x - 1, fx - 1, -1):
            if maze[i][y] != "F": #Makes sure F doesn't get replaced
                maze[i][y] = "."

    if y < fy:
        for i in range(y + 1, fy + 1):
            if maze[fx][i] != "F": #Makes sure F doesn't get replaced
                maze[fx][i] = "."
    elif y > fy:
        for i in range(y - 1, fy - 1, -1):
            if maze[fx][i] != "F": #Makes sure F doesn't get replaced
                maze[fx][i] = "."

if __name__ == "__main__":
    main()
