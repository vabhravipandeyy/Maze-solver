# Maze Solver using A* Algorithm in Python

## Project Overview

This project implements a **Maze Solver** using the **A* (A-Star) path-finding algorithm** in Python.
The program finds the **shortest path** from a **start point** to a **goal point** inside a grid-based maze while avoiding walls.

This project demonstrates **basic Artificial Intelligence pathfinding**, **data structures**, and **algorithmic problem solving**.

##  Objective

To design and implement a Python program that computes the **optimal shortest path** in a maze using the **A* search algorithm**.

##  Key Concepts Used

* Python programming
* A* search algorithm
* Heuristic function (Manhattan distance)
* Priority queue using `heapq`
* Grid-based pathfinding

##  Maze Representation

* `0` → Free path
* `1` → Wall/blocked cell
* Start position → `(0, 0)`
* Goal position → `(3, 3)`

##  How the Algorithm Works

1. Start node is added to the **open list**.
2. The node with the **lowest cost** `f(n) = g(n) + h(n)` is selected.
3. Neighboring valid cells are explored.
4. Costs and parent nodes are updated if a **better path** is found.
5. Process continues until the **goal node** is reached.
6. The final **shortest path** is reconstructed.

##  Real-World Applications

* Google Maps navigation
* Game AI pathfinding
* Robot motion planning
* Network routing systems

##  Advantages

* Guarantees **shortest path**
* Efficient with a **good heuristic**
* Widely used in **AI and robotics**

##  Limitations

* Performance depends on **heuristic quality**
* May use **higher memory** for very large mazes

##  Future Improvements

* Add **graphical visualization using Pygame**
* Allow **user-generated maze input**
* Compare **A*, BFS, and Dijkstra algorithms**
* Build a **web-based interface**

##  Author

**Vabhravi Pandey**
B.Tech CSE (AIML)

⭐ If you like this project, consider giving it a **star** on GitHub!
