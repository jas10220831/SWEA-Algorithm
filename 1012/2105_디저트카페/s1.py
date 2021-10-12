import sys
sys.stdin = open('sample_input.txt')


# 대각선 방향으로 이동해서 제자리로 돌아온다.
# 방향전환이 3번 일어나야 된다.

dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]

def make_root(numbers, start, now, desert_list = [], drift = 0):
    global answer

    # 방향 전환이 4번 이상 일어날 경우
    # 이미 방문한 가게 종류일 경우
    if drift > 3:
        return

    # 출발 후 마지막으로 출발지점으로 돌아왔을 경우
    if drift == 3 and now == start:
        if answer < len(desert_list):
            answer = len(desert_list)
        print('end')
        return
    else:
        print(now)
        print(dy[drift], dx[drift])
        new_y = now[0] + dy[drift]
        new_x = now[1] + dx[drift]
        if 0 <= new_y < N and 0 <= new_x < N and not numbers[new_y][new_x] in desert_list:
            # 방문표시
            # 디저트 가게 표시
            desert_list.append(numbers[new_y][new_x])
            # 방향 전환 안할 경우
            make_root(numbers, start, [new_y, new_x], desert_list, drift)
            # 방향 전환 할 경우
            make_root(numbers, start, [new_y, new_x], desert_list, drift+1)
            # 표시 한것들 초기화
            desert_list.pop()



T = int(input())
for t in range(1, 2):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    answer = -1
    for i in range(N):
        for j in range(N):
            print('start')
            make_root(numbers, [i, j], [i, j])
    print('#{} {}'.format(t, answer))