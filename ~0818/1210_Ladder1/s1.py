import sys
sys.stdin = open('input.txt')

# 1. 밑으로 내려가는 변수는 특별히 조작할 필요없이 1씩 더해주기만 한다.
# 2. 왼쪽 오른쪽 상태를 본다.


for _ in range(10):
    T = int(input())
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))
    # 처음 값이 출발지점들을 나타낸다.
    for idx, i in enumerate(ladder[0]):
        # i 가 1일 경우 출발
        if i:
            # 왼쪽 오른쪽 이동시킬 변수
            move = idx
            # 아래로 이동시키는 변수
            down = 0
            # 아래로 내려가기 시작한다.
            while down != 99:
                # 왼쪽으로 이동할 경우
                # 왼쪽의 값이 1인 경우
                # ladder[down][move] 현재 위치
                if move-1 >= 0 and ladder[down][move-1]:
                    # 1이 아닐 때까지 이동
                    while move-1 >= 0 and ladder[down][move-1]:
                        move -= 1
                    down += 1
                # 오른쪽으로 이동할 경우
                elif move+1 <= 99 and ladder[down][move+1]:
                    while move+1 <= 99 and ladder[down][move+1]:
                        move += 1
                    down += 1
                else:
                    down += 1
            if ladder[down][move] == 2:
                print('#{} {}'.format(T, idx))
                break



