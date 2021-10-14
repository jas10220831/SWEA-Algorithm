import sys
sys.stdin = open('sample_input.txt')

from collections import deque

# 우, 하, 좌, 상
dy = [0, 1, 0 ,-1]
dx = [1, 0, -1, 0]

def BFS(start):

    Q = deque()
    Q.append(start)
    costs[start[0]][start[1]] = 0

    while Q:
        now = Q.popleft()
        for i in range(4):
            new_y = now[0] + dy[i]
            new_x = now[1] + dx[i]
            if 0 <= new_y < N and 0 <= new_x < N:
                cost = matrix[new_y][new_x] - matrix[now[0]][now[1]]
                # 다음 위치가 더 높을 경우
                if cost > 0:
                    cost += 1
                else:
                    cost = 1
                # 이동하려는 곳에 저장된 비용이 현재 비용보다 클경우 교체
                if costs[new_y][new_x] > cost + costs[now[0]][now[1]]:
                    costs[new_y][new_x] = cost + costs[now[0]][now[1]]
                    Q.append([new_y, new_x])
    return costs[N-1][N-1]



T = int(input())
for t in range(1, T+1):
    N = int(input())
    #노드 개수
    V = N * N
    matrix = [list(map(int, input().split())) for _ in range(N)]
    costs = [[100000] * N for _ in range(N)]
    print('#{} {}'.format(t,BFS([0, 0])))