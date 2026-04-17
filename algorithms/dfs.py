import pygame

def dfs(draw, grid, start, end):
    stack = [start]
    came_from = {}
    visited = {start}

    while stack:
        pygame.event.pump()

        current = stack.pop()

        if current == end:
            reconstruct(came_from, end, draw)
            start.make_start()
            end.make_end()
            return True

        for n in current.neighbors:
            if n not in visited:
                visited.add(n)
                came_from[n] = current
                stack.append(n)
                n.make_visited()

        draw()

    return False


def reconstruct(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()