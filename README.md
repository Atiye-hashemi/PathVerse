![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)

![Pygame](https://img.shields.io/badge/Pygame-2.x-green)

![Status](https://img.shields.io/badge/Status-Completed-success)

![License](https://img.shields.io/badge/License-MIT-yellow)



### PathVerse — Pathfinding Visualizer

PathVerse is an interactive visualization tool that demonstrates how different pathfinding algorithms explore a grid to find the shortest path between two points.

It helps users visually understand how algorithms like BFS, DFS, and Dijkstra behave in real time.

---


Features

- Interactive grid system
- Place start and end nodes
- Draw/remove walls using mouse
- Visualize algorithms in real time
- Supports:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Dijkstra’s Algorithm

---

Algorithms Explained

BFS (Breadth-First Search)
- Explores level by level
- Guarantees shortest path in unweighted graphs

DFS (Depth-First Search)
- Goes deep before exploring neighbors
- Does NOT guarantee shortest path

Dijkstra’s Algorithm
- Uses priority-based exploration
- Guarantees shortest path with weighted logic

---

Tech Stack

- Python
- Pygame

---

How to Run

```bash
pip install -r requirements.txt
python main.py
