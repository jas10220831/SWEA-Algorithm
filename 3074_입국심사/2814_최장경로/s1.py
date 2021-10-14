import sys
sys.stdin = open('sample_input.txt')


# 일단 DFS 완전탐색으로 해보자
def longest(graph, start):
    global answer

    # 방문표시
    visited[start] = 1
    # 크기 비교
    answer = max(answer, sum(visited))

    # 재귀로 DFS 실행
    for idx, bo in enumerate(graph[start]):
        # 간선 존재하고 방문 안함
        if bo and not visited[idx]:
            longest(graph, idx)
    # 방문표시를 풀어준다.
    visited[start] = 0

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    # 인접 그래프로 해볼까?
    graph = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        i, j = map(int, input().split())
        graph[i][j] = 1
        graph[j][i] = 1
    visited = [0] * (N+1)
    answer = 0
    for i in range(1, N+1):
        # 1번 노드부터 끝까지 완전 탐색
        longest(graph, i)
    print('#{} {}'.format(t, answer))