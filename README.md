# Random maze generator and solver
#### Description:
The Random Maze Generator and Solver is a Python-based project that creates a randomized maze and solves it using two distinct algorithms. The goal is to allow users to see a generated maze and compare the efficiency of two pathfinding approaches: Depth-First Search (DFS) and Direct Path algorithms. This project offers a simple menu-based interface where users can create a maze of desired dimensions, run one or both algorithms to solve the maze, and view their runtime for comparison.

## Project Structure:
-main(): The entry point for the program, initiating the user menu.
-choose_an_algorithm(): Provides a menu for the user to select options, such as running DFS, Direct Path, or comparing both algorithms.
-get_width_height(): Prompts users to input the maze's dimensions, ensures odd values for better algorithm compatibility, and returns the maze size.
-create_maze(): Initializes a 2D maze of walls (#), randomly places a start (S) and a finish (F) position, and returns the maze structure.
-depth_first_search(): A recursive function that uses DFS to carve out a path in the maze by exploring random directions and marking traversable paths with ..
-direct_path(): Creates a straight line from the start to finish, providing an efficient but less interesting path than DFS.

## Design choices:

### Functional programming:
Pure Functions: Many of the functions, such as create_maze, depth_first_search, and direct_path, are designed to produce outputs solely based on their inputs without side effects. This makes them reliable and predictable.
Immutability: While Python doesn’t enforce immutability strictly, my project minimizes changes to global states and focuses on local state changes within functions, especially in functions like depth_first_search, which operates recursively without relying on external variables.
Modularity and Composition: Each function is responsible for a specific task, whether it’s generating a maze, handling user input, or solving the maze. This separation allows functions to be composed and reused, improving the overall modularity of the code.

### Program Flow:
Menu Interface: After getting height and width from the user, the menu allows algorithm selection, providing flexibility in how the maze is generated and solved.
Depth-First Search Algorithm: Designed to carve paths in random directions, making each maze unique. It’s an exploration algorithm that ensures paths don’t overlap, enhancing maze complexity.
Direct Path Algorithm: Used for comparison, it creates a fast, direct path from start to finish, making it much faster than DFS but less intricate.
Runtime Comparison: In Option 3, both algorithms run consecutively, allowing users to see time differences, giving insight into algorithm efficiency.

## Future Improvements:
Additional Algorithms: Implementing other pathfinding algorithms, such as A* or Breadth-First Search (BFS), would enhance the project and provide further insights into algorithmic performance.
Maze Complexity Options: Allowing users to specify the complexity or branching factor could create more challenging or simplistic mazes.
Visualization: Creating a graphical interface to visualize maze generation and solution paths would improve user engagement.

## Conclusions:
Additional Algorithms: Implementing other pathfinding algorithms, such as A* or Breadth-First Search (BFS), would enhance the project and provide further insights into algorithmic performance.
Maze Complexity Options: Allowing users to specify the complexity or branching factor could create more challenging or simplistic mazes.
Visualization: Creating a graphical interface to visualize maze generation and solution paths would improve user engagement.
