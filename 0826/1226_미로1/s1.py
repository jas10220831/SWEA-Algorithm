import sys
sys.stdin = open('input.txt')

def find_road(maze):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[0] * 17 for _ in range(17)]
    start = [1, 1]
    queue = [start]
    while queue:
        now = queue.pop(0)
        visited[now[0]][now[1]] += 1
        for i in range(4):
            new_x = now[1] + dx[i]
            new_y = now[0] + dy[i]
            if not maze[new_y][new_x] and not visited[new_y][new_x]:
                queue.append([new_y, new_x])
            if maze[new_y][new_x] == 3:
                return 1
    return 0


for t in range(1, 11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    print('#{} {}'.format(T, find_road(maze)))
