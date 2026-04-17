import pygame
from grid import create_grid
from ui import Button
from utils.colors import *
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.dijkstra import dijkstra

pygame.init()


# CONFIG

WIDTH = 600
ROWS = 20
CELL_SIZE = WIDTH // ROWS
UI_HEIGHT = 60

WIN = pygame.display.set_mode((WIDTH, WIDTH + UI_HEIGHT))
pygame.display.set_caption("PathVerse")

DELAY = 20



# DRAW FUNCTION

def draw(win, grid, buttons):
    win.fill(WHITE)

    # UI BAR
    pygame.draw.rect(win, UI_BG, (0, 0, WIDTH, UI_HEIGHT))

    for b in buttons:
        b.draw(win)

    # GRID (shifted down)
    for row in grid:
        for node in row:
            pygame.draw.rect(
                win,
                node.color,
                (node.x, node.y + UI_HEIGHT, CELL_SIZE, CELL_SIZE)
            )

    # GRID LINES
    for i in range(ROWS):
        pygame.draw.line(
            win,
            GREY,
            (0, i * CELL_SIZE + UI_HEIGHT),
            (WIDTH, i * CELL_SIZE + UI_HEIGHT)
        )
        pygame.draw.line(
            win,
            GREY,
            (i * CELL_SIZE, UI_HEIGHT),
            (i * CELL_SIZE, WIDTH + UI_HEIGHT)
        )

    pygame.display.update()



# GET CLICK POSITION

def get_pos(pos):
    x, y = pos

    if y < UI_HEIGHT:
        return None

    y -= UI_HEIGHT
    return y // CELL_SIZE, x // CELL_SIZE



# CLEAR SEARCH ONLY

def clear_search(grid):
    for row in grid:
        for n in row:
            if n.color in [PINK, BLUE]:
                n.reset()



# MAIN

def main():
    global DELAY

    grid = create_grid(ROWS, CELL_SIZE)
    start = None
    end = None

    buttons = []

   
    # WRAPPERS
    
    def run_bfs():
        for row in grid:
            for n in row:
                n.update_neighbors(grid, ROWS)
        bfs(lambda: draw(WIN, grid, buttons), grid, start, end)

    def run_dfs():
        for row in grid:
            for n in row:
                n.update_neighbors(grid, ROWS)
        dfs(lambda: draw(WIN, grid, buttons), grid, start, end)

    def run_dijkstra():
        for row in grid:
            for n in row:
                n.update_neighbors(grid, ROWS)
        dijkstra(lambda: draw(WIN, grid, buttons), grid, start, end)

    def clear_all():
        nonlocal grid, start, end
        grid = create_grid(ROWS, CELL_SIZE)
        start = None
        end = None

   
    # BUTTONS
  
    buttons.append(Button(10, 10, 100, 40, "BFS", run_bfs))
    buttons.append(Button(120, 10, 100, 40, "DFS", run_dfs))
    buttons.append(Button(230, 10, 120, 40, "Dijkstra", run_dijkstra))
    buttons.append(Button(370, 10, 100, 40, "Clear", clear_all))

    run = True

    
    # LOOP
   
    while run:
        draw(WIN, grid, buttons)

        left, _, right = pygame.mouse.get_pressed()

        
        # CONTINUOUS DRAW
        
        if left:
            pos = pygame.mouse.get_pos()
            result = get_pos(pos)
            if result:
                r, c = result
                node = grid[r][c]
                if node != start and node != end:
                    node.make_wall()

        if right:
            pos = pygame.mouse.get_pos()
            result = get_pos(pos)
            if result:
                r, c = result
                node = grid[r][c]
                node.reset()

        
        # EVENTS
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # button clicks
                for b in buttons:
                    b.click(pos)

                result = get_pos(pos)
                if result:
                    r, c = result
                    node = grid[r][c]

                    if not start:
                        start = node
                        start.make_start()

                    elif not end:
                        end = node
                        end.make_end()

            if event.type == pygame.KEYDOWN:

                # SPACE → clear only search
                if event.key == pygame.K_SPACE:
                    clear_search(grid)

                # BFS
                if event.key == pygame.K_b and start and end:
                    run_bfs()

                # DFS
                if event.key == pygame.K_d and start and end:
                    run_dfs()

                # DIJKSTRA
                if event.key == pygame.K_j and start and end:
                    run_dijkstra()

                # speed control
                if event.key == pygame.K_UP:
                    DELAY = max(1, DELAY - 5)

                if event.key == pygame.K_DOWN:
                    DELAY += 5

    pygame.quit()


if __name__ == "__main__":
    main()