from node import Node

def create_grid(rows, cell_size):
    grid = []
    for r in range(rows):
        grid.append([])
        for c in range(rows):
            grid[r].append(Node(r, c, cell_size))
    return grid