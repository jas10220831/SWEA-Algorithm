import sys
sys.stdin = open('sample_input.txt')

import copy


def delete(temp, y, x):
    bomb_range= temp[y][x]
    Q = []
    Q.append((y, x, bomb_range))
    temp[y][x] = 0
    while Q:
        now_y, now_x, now_range = Q.pop(0)
        # 폭발 범위 만큼 늘려가면서 델타 탐색
        for i in range(now_range):
            for j in range(4):
                new_y = now_y + (dy[j] * i)
                new_x = now_x + (dx[j] * i)
                if 0 <= new_x < W and 0 <= new_y < H and temp[new_y][new_x]:
                    Q.append((new_y, new_x, temp[new_y][new_x]))
                    temp[new_y][new_x] = 0


def new_bricks(bricks):
    for c in range(W):
        for r in range(H - 1, -1, -1):
            if bricks[r][c] == 0:
                for step in range(r - 1, -1, -1):
                    if bricks[step][c] != 0:
                        bricks[r][c], bricks[step][c] = bricks[step][c], 0
                        break
                else:
                    break


def broken(bricks, k=0):
    global answer

    # 남은 블록 개수 구하기
    if k == N:
        result = W * H
        for i in range(H):
            result -= bricks[i].count(0)
        if result < answer:
            answer = result
        return

    # 블록 지우기
    for i in range(W):
        for j in range(H):
            if bricks[j][i]:
                # TODO 블록 지우기
                temp = copy.deepcopy(bricks)
                delete(temp, j, i)
                # TODO 블록 정렬
                new_bricks(temp)
                broken(temp, k+1)
                break


T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    problem = [list(map(int, input().split())) for _ in range(H)]
    answer = W * H
    # 우, 하, 좌, 상
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    broken(problem)
    if answer == W * H:
        answer= 0
    print('#{} {}'.format(t, answer))