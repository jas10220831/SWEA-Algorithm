import sys
sys.stdin = open('input.txt')


def Dijkstra():
    cost = [9876543210000] * N
    visited = [0] * N
    cost[0] = 0
    for _ in range(N):
        minidx = -1
        minV = 9876543210000
        for i in range(N):
            if not visited[i] and cost[i] < minV:
                minidx = i
                minV = cost[i]
        visited[minidx] = 1
        for i in range(N):
            if not visited[i] and graph[minidx][i]< cost[i]:
                cost[i] = graph[minidx][i]
    return round(sum(cost))

T = int(input())
for t in range(1, T+1):
    N = int(input())
    X_list = list(map(int, input().split()))
    Y_list = list(map(int, input().split()))
    E = float(input())
    graph = [[0] * N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            cost = E * ((X_list[i] - X_list[j]) ** 2 + ((Y_list[i] - Y_list[j])) ** 2)
            graph[i][j] = cost
            graph[j][i] = cost
    print('#{} {}'.format(t, Dijkstra()))