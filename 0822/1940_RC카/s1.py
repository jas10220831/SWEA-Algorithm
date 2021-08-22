import sys
sys.stdin = open('input.txt')

def meter(N, commands):
    answer = 0
    speed = 0
    for idx, command in enumerate(commands):
        # 가속하는 경우
        # 속도가 0 이상일 경우에만 움직인다.
        if command[0] == 1 and speed >= 0:
            speed += command[1]
        # 감속하는 경우
        elif command[0] == 2:
            if speed > command[1]:
                speed -= command[1]
            else:
                speed = 0
        answer += speed
    # 가속도가 더 커서 정지할 경우
    return answer


T = int(input())

for t in range(1, T+1):
    N = int(input())
    commands = []
    for _ in range(N):
        commands.append(list(map(int, input().split())))
    print('#{} {}'.format(t, meter(N, commands)))