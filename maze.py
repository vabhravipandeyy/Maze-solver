from heapq import heappush, heappop

maze = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
end = (3, 3)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar():
    open_list = []
    heappush(open_list, (0, start))
    came_from = {}
    cost = {start: 0}

    while open_list:
        _, current = heappop(open_list)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            next_node = (current[0]+dx, current[1]+dy)

            if (0 <= next_node[0] < len(maze) and
                0 <= next_node[1] < len(maze[0]) and
                maze[next_node[0]][next_node[1]] == 0):

                new_cost = cost[current] + 1

                if next_node not in cost or new_cost < cost[next_node]:
                    cost[next_node] = new_cost
                    priority = new_cost + heuristic(end, next_node)
                    heappush(open_list, (priority, next_node))
                    came_from[next_node] = current

    return None

print("Shortest path:", astar())