from collections import deque
import pygame

def bfs(draw, grid, start, end):
    queue = deque([start])
    came_from = {}
    visited = {start}

    while queue:
        pygame.event.pump()

        current = queue.popleft()

        if current == end:
            reconstruct(came_from, end, draw)
            start.make_start()
            end.make_end()
            return True

        for n in current.neighbors:
            if n not in visited:
                visited.add(n)
                came_from[n] = current
                queue.append(n)
                n.make_visited()

        draw()

    return False


def reconstruct(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()