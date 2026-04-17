import pygame
from utils.colors import *

class Node:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size
        self.x = col * size
        self.y = row * size
        self.color = WHITE
        self.neighbors = []

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))

    def is_wall(self): return self.color == BLACK
    def is_start(self): return self.color == GREEN
    def is_end(self): return self.color == RED

    def make_start(self): self.color = GREEN
    def make_end(self): self.color = RED
    def make_wall(self): self.color = BLACK
    def make_visited(self):
        if not self.is_start() and not self.is_end():
            self.color = PINK

    def make_path(self):
        if not self.is_start() and not self.is_end():
            self.color = BLUE

    def reset(self):
        self.color = WHITE

    def update_neighbors(self, grid, rows):
        self.neighbors = []

        if self.row < rows - 1 and not grid[self.row + 1][self.col].is_wall():
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < rows - 1 and not grid[self.row][self.col + 1].is_wall():
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
            self.neighbors.append(grid[self.row][self.col - 1])