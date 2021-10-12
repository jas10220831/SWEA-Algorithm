import sys
sys.stdin = open('sample_input.txt')

import copy

# 여기서 문제가 발생하는 것 같다
# 얕은 복사가 되는거 같기도 하고
# 방법을바꾸자
def new_bricks(bricks):
    for i in range(W):
        for j in range(H-1, 0, -1):
            # 밑에가 0이라면
            if not bricks[j][i]:
                # 위에서 0이 아닌 숫자를 찾아서 바꾼다.
                h = j
                while h >= 0 and not bricks[h][i]: h -= 1
                # 이 부분을 추가하닌까 문제가 풀렸다.
                # 뭐가 다른거지?
                if h >= 0 and bricks[h][i]:
                    bricks[j][i], bricks[h][i] = bricks[h][i], bricks[j][i]
    return bricks


def delete(bricks, y, x):
    # 위치
    Q = []
    Q.append((y, x, bricks[y][x]))
    while Q:
        y, x, bomb_range = Q.pop(0)
        bricks[y][x] = 0
        # 범위 탐색하면서 0으로 바꾸고 1보다 크면 연쇄반응
        # delta 탐색
        for bomb in range(1, bomb_range):
            # 4방향으로 연쇄반응 크기를 1 부터 1씩 늘려가면서 탐색
            for delta in range(4):
                new_y = y + (dy[delta] * bomb)
                new_x = x + (dx[delta] * bomb)
                if 0 <= new_y < H and 0 <= new_x < W and bricks[new_y][new_x]:
                    Q.append((new_y, new_x, bricks[new_y][new_x]))
                    bricks[new_y][new_x] = 0


def broken(bricks, k=0):
    global answer

    if k == N:
        result = W * H
        for i in range(H):
            result -= bricks[i].count(0)
        if result < answer:
            answer = result
        return

    # 출발지점 찾기
    for i in range(W):
        for j in range(H):
            # 벽돌 처음으로 깨질 장소 발견
            if bricks[j][i]:
                # 깊은 복사
                temp = copy.deepcopy(bricks)
                delete(temp, j, i)
                new = new_bricks(temp)
                broken(new, k+1)
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