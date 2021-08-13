import sys
sys.stdin = open('input.txt')

# 아래에서 위로 올라가는 방법


for _ in range(10):
    T = int(input())
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))
    # 처음 값이 출발지점들을 나타낸다.
    ladder[0] = list(range(100))
    for idx, i in enumerate(ladder[-1]):
        # i 가 2일 경우 출발
        if i == 2:
            # 왼쪽 오른쪽 이동시킬 변수
            move = idx
            # 위로 이동시키는 변수
            up = 99
            # 위로 올라가기 시작한다..
            while up != 0:
                # 왼쪽으로 이동할 경우
                # 왼쪽의 값이 1인 경우
                if move-1 >= 0 and ladder[up][move-1]:
                    # 0이 아닐 때까지 이동
                    while move-1 >= 0 and ladder[up][move-1]:
                        move -= 1
                    up -= 1
                # 오른쪽으로 이동할 경우
                elif move+1 <= 99 and ladder[up][move+1]:
                    while move+1 <= 99 and ladder[up][move+1]:
                        move += 1
                    up -= 1
                else:
                    up -= 1
            print('#{0} {1}'.format(T, ladder[0][move]))



