import sys
sys.stdin = open('sample_input.txt')


def Prim(N, start=0):
    pi = [None] * (N+1)
    MST = [0] * (N+1)
    key = [11] * (N+1)
    key[start] = 0

    # 모든 정점이 MST에 포함될 때까지 반복
    for _ in range(N+1):
        u = 0
        minV = 11
        for i in range(N+1):
            # 아직 포함되지 않은 노드일 경우
            if MST[i] == 0:
                if key[i] < minV:
                    u = i
                    minV = key[i]
        MST[u] = 1
        for n in range(N+1):
            # 아직 MST에 포함되어 있지 않고 경로가 존재하는 경우
            if MST[n] == 0 and graph[u][n] != 0:
                # 기존 연결된 경로보다 새로운 경로의 가중치가 적을 경우 교체
                if key[n] > graph[u][n]:
                    key[n] = graph[u][n]
                    pi[n] = u # 연결된 정점 포함
    return sum(key)



T = int(input())
for t in range(1, T+1):
    # N 마지막 노드 번호 즉 노드 개수는 N+1 개
    N, M = map(int, input().split())
    graph = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        n1, n2, w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w
    print('#{} {}'.format(t,Prim(N)))