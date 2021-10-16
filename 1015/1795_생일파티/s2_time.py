import sys
sys.stdin = open('input.txt')


def find(start, flag=0):
    visited = [0] * (N+1)
    time = [float('inf')] * (N+1)
    time[start] = 0
    pi = [None]

    for _ in range(N):
        minV = float('inf')
        minidx = -1
        for i in range(1, N+1):
            if not visited[i] and time[i] < minV:
                minidx = i
                minV = time[i]
        visited[minidx] = 1
        pi.append(minidx)
        # 처음 1~N 부터 X로 가는 경우
        if flag:
            # 목적지에 도착했을 경우
            if minidx == X:
                # 그 때의 거리값 출력
                return time, minV, visited, pi
        for i in range(1, N+1):
            if road[minidx][i]:
                if not visited[i] and road[minidx][i] + time[minidx] < time[i]:
                    time[i] = road[minidx][i] + time[minidx]
    return time

def cacul():
    X_to_N = find(X)
    time_cost = [-1]
    answer = 0
    for i in range(1, N+1):
        (time, N_to_X, visited, pi) = find(i, 1)
        print(i)
        print(time)
        print(visited)
        print(N_to_X)
        print(pi)
        print(time[X] == N_to_X)
        print('-------------------')
        if answer < N_to_X + X_to_N[i]:
            answer = N_to_X + X_to_N[i]
    return answer


T = int(input())
for t in range(1, 3):
    N, M, X = map(int, input().split())
    road = [[0]*(N+1) for _ in range(N+1)]
    print(X)
    for _ in range(M):
        x, y, c = map(int, input().split())
        road[x][y] = c

    print('#{} {}'.format(t,cacul()))
