import sys
sys.stdin = open('sample_input.txt')
from collections import deque

def cacul(N, idx):
    if idx == 0:
        return N * 2
    elif idx == 1:
        return N - 1
    elif idx == 2:
        return N - 10
    else:
        return N + 1


def find():

    Q = deque()
    visited = [N]
    Q.append([N, 0])

    while Q:
        now = Q.popleft()
        if now[0] == M:
            return now[1]

        for i in range(4):
            new = cacul(now[0], i)
            if not new in visited and not new <= 0 and not new > 1000000:
                visited.append(new)
                Q.append([new, now[1]+1])


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    print('#{} {}'.format(t, find()))

