import sys
sys.stdin = open('sample_input.txt')

# 우, 하, 좌, 상
dy = [0, 1, 0 ,-1]
dx = [1, 0, -1, 0]

# 행렬을 그래프로 바꾸는 함수
def mx_gr(matrix):
    graph = [[0] * (N * N) for _ in range(N * N)]

    # 델타탐색 시작
    # 현재 노드에서 연결된 노드의 위치
    for i in range(N):
        for j in range(N):
            for delta in range(4):
                new_y = i + dy[delta]
                new_x = j + dx[delta]
                # 그래프 상에서 현재 노드 번호
                node = N * i + j
                # 그래프 상에서 현재 노드에서 연결된 노드 번호들
                dn = [node + 1, node + N, node - 1, node - N]
                # 범위 안의 좌표라면
                if 0 <= new_y < N and 0 <= new_x < N and 0 <= dn[delta] < N*N:
                    # 비용 계산
                    # 현재 위치보다 낮을 경우
                    if matrix[i][j] >= matrix[new_y][new_x]:
                        cost = 1
                    else: # 현재 위치보다 높을 경우
                        cost = matrix[new_y][new_x] - matrix[i][j] + 1
                    graph[node][dn[delta]] = cost
    return graph

def Dijkstar(graph, start= 0):
    D = [101] * V
    visited = [0] * V
    D[start] = 0
    for _ in range(V):
        idx = 0
        minV = 101
        for i in range(V):
            if not visited[i] and D[i] < minV:
                idx = i
                minV = D[i]
        visited[idx] = 1
        for i, cost in enumerate(graph[idx]):
            if cost and not visited[i]:
                if D[idx] + cost < D[i]:
                    D[i] = D[idx] + cost
    return D




T = int(input())
for t in range(1, T+1):
    N = int(input())
    #노드 개수
    V = N * N
    matrix = [list(map(int, input().split())) for _ in range(N)]
    graph = mx_gr(matrix)
    print('#{} {}'.format(t,Dijkstar(graph)[-1]))
