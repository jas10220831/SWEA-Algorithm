import sys
sys.stdin = open('input.txt')
from collections import deque


def rebuild(road):
    Q = deque()
    Q.append([0, 0])
    dy = [0, -1 ,0 ,1]
    dx = [1, 0 ,-1 ,0]
    cost = [[1000] * N for _ in range(N)]
    cost[0][0] = 0


    while Q:
        now = Q.popleft()
        for idx in range(4):
            new_y = now[0] + dy[idx]
            new_x = now[1] + dx[idx]
            # 범위 내 존재 아직 방문 안함
            if 0 <= new_y < N and 0 <= new_x < N:
                # 비용 계산
                if cost[now[0]][now[1]] + road[new_y][new_x] < cost[new_y][new_x]:
                    cost[new_y][new_x] = cost[now[0]][now[1]] + road[new_y][new_x]
                    Q.append([new_y, new_x])
    return cost[N-1][N-1]

# 어차피 비용이 더 적을 경우에만 이동한다. -> 이걸 고려 안하면 시간초과

T = int(input())
for t in range(1, T+1):
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)]
    print('#{} {}'.format(t, rebuild(road)))