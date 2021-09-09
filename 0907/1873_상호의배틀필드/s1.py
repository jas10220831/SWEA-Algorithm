import sys
sys.stdin = open('input.txt')


def battlefield(height, width, maps, controls):
    '''
    문자 의미
    .	평지(전차가 들어갈 수 있다.)
    *	벽돌로 만들어진 벽 -> 포탄에 맞으면 평지(.)로 바뀐다.
    #	강철로 만들어진 벽
    -	물(전차는 들어갈 수 없다.)
    ^	위쪽을 바라보는 전차(아래는 평지이다.)
    v	아래쪽을 바라보는 전차(아래는 평지이다.)
    <	왼쪽을 바라보는 전차(아래는 평지이다.)
    >	오른쪽을 바라보는 전차(아래는 평지이다.)
    U, D, L, R, S
    :param maps:
    :param controls:
    :return:
    '''
    moves = ['^', 'v', '<', '>']
    # 1. 전차의 현재 위치를 특정
    for i in range(height):
        for j in range(width):
            if maps[i][j] in moves:
                # y축, x축, 전차가 현재 바라보는 방향
                now = [i, j, map[i][j]]
                break


    # 일일히 조건문을 넣어서 하기에는 코드가 보기 별로
    # 각 방향 으로 사격 한 결과를 돌려주는 함수 각각 생성
    # 함수 return 값은 map을 돌려주자.
    # 윗쪽으로 사격 결과
    def shoot_up(maps, now):
        pass
    # 아래쪽으로 사격 결과
    def shoot_down(maps, now):
        pass
    # 왼쪽으로 사격 결과
    def shoot_left(maps, now):
        pass
    # 오른쪽으로 사격 결과
    def shoot_right(maps, now):
        pass

    # 전차의 방향 조작 및 움직이는 함수
    def move_to(maps, now, control):
        y = now[0]
        x = now[1]
        if control == 'U':
            # 전차 방향 전환
            now[2] = '^'
            while True:
                # 위쪽으로 이동 가능 확인
                # 평지일 경우
                if  maps[y-1][x] >=0 and maps[y-1][x] == '.':
                    # 전차 한칸 위로 이동
                    y -= 1
                    now[0] = y
                    maps[y][x] = '^'
                    # 전차가 있던 자리는 평지로
                    maps[y][x] = '.'
                else:
                    break
        elif control == 'D':
            now[2] = 'v'
            while True:




    # 2. 명령어 수행 시작
    for control in controls:
        # shoot 현재 바라보고 있는 방향으로 사격
        if control == 'S':
            # 현재 방향에 대한 정보 필요
            now[2]
            # 경로에 대한 정보 필요
        # 방향 전환 및 이동
        else:
            move_to(maps, now, control)




T = int(input())
for t in range(1, T+1):
    height, width = map(int, input().split())
    maps = []
    for _ in range(height):
        maps.append(list(map(str, input())))
    N = int(input())
    controls = list(map(str, input()))

