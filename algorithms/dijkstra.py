import heapq
import pygame

def dijkstra(draw, grid, start, end):
    count = 0
    pq = []
    heapq.heappush(pq, (0, count, start))

    distances = {node: float("inf") for row in grid for node in row}
    distances[start] = 0

    came_from = {}

    while pq:
        pygame.event.pump()

        current = heapq.heappop(pq)[2]

        if current == end:
            reconstruct(came_from, end, draw)
            start.make_start()
            end.make_end()
            return True

        for n in current.neighbors:
            temp = distances[current] + 1

            if temp < distances[n]:
                distances[n] = temp
                came_from[n] = current
                count += 1
                heapq.heappush(pq, (temp, count, n))
                n.make_visited()

        draw()

    return False


def reconstruct(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()