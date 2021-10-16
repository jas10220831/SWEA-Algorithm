import sys
sys.stdin = open('input.txt')


def find(start, graph):
    visited = [0] * (N+1)
    time = [987654321] * (N+1)
    time[start] = 0

    for _ in range(N):
        minV = 987654321
        minidx = -1
        for i in range(1, N+1):
            if not visited[i] and time[i] < minV:
                minidx = i
                minV = time[i]
        visited[minidx] = 1
        for i in range(1, N+1):
            if graph[minidx][i]:
                if not visited[i] and graph[minidx][i] + time[minidx] < time[i]:
                    time[i] = graph[minidx][i] + time[minidx]
    return time

# 길을 뒤집으면 각 장소에서 목표 장소로 오는 함수가 만들어 진다.

def cacul():
    answer = 0
    X_to_N = find(X, road1)
    N_to_x = find(X, road2)
    for i in range(1, N+1):
        now = X_to_N[i] + N_to_x[i]
        if now > answer:
            answer = now
    return answer

T = int(input())
for t in range(1, T+1):
    N, M, X = map(int, input().split())
    road1 = [[0]*(N+1) for _ in range(N+1)]
    road2 = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        road1[x][y] = c
        road2[y][x] = c
    print('#{} {}'.format(t, cacul()))

