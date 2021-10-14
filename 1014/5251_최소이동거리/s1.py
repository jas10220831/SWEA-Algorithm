import sys
sys.stdin = open('sample_input.txt')


def answer(graph):
    cost = [1001] * (N+1)
    visited = [0] * (N+1)
    # 0 -> N으로 가므로 맨처음 출발지 비용 0
    cost[0] = 0

    for _ in range(N+1):
        minidx = -1
        minV = 1001

        # 현재 트리 근접 노드에서 비용이 가장 작은 노드 찾기
        for i in range(N+1):
            if not visited[i] and cost[i] < minV:
                minV = cost[i]
                minidx = i
        visited[minidx] = 1
        # 이동시 최소 비용 최신화
        for idx, new_cost in enumerate(graph[minidx]):
            if new_cost:
                if not visited[idx] and new_cost + cost[minidx] < cost[idx]:
                    cost[idx] = new_cost + cost[minidx]
    return cost[-1]


T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    graph =[[0] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
    print('#{} {}'.format(t, answer(graph)))

