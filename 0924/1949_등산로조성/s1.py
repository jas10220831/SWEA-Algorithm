import sys
sys.stdin = open('sample_input.txt')

# 결국 DFS는 하나의 출발점, 하나의 지도, 하나의 방문표시로 시작해야한다.
# 처음에는 3개의 출발점에서 지도, 방문표시를 모두 공유해서 답이 안나왔다.
# DFS, BFS 모두 출발점은 하나라는 점을 생각하면서 문제를 풀어야 겠다.

def road(y, x, length, check):
    global answer
    if length > answer:
        answer = length

    visited[y][x] = 1
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0 <= new_y < N and 0 <= new_x < N and not visited[new_y][new_x]:
            # 낮아서 이동할 수 있는 경우
            if maps[new_y][new_x] < maps[y][x]:
                road(new_y, new_x, length + 1, check)
            else:
                if check and maps[new_y][new_x] - K < maps[y][x]:
                    tmp = maps[new_y][new_x]
                    maps[new_y][new_x] = maps[y][x] - 1
                    road(new_y, new_x, length + 1, 0)
                    maps[new_y][new_x] = tmp
    visited[y][x] = 0



T = int(input())
for t in range(1, T+1):
    # N: 지도의 크기, K: 공사 가능한 높이
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    answer = -1
    max_height = 0
    # max(max(maps)) 하닌까 답이 틀렸다 뭐가 다른거지?
    # 되는게 있고 안되는게 있는데....
    for i in range(N):
        for j in range(N):
            if maps[i][j] > max_height:
                max_height = maps[i][j]

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    for i in range(N):
        for j in range(N):
            if maps[i][j] == max_height:
                road(i, j, 1, 1)
    print('#{} {}'.format(t, answer))