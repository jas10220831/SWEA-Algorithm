import sys
sys.stdin = open('sample_input.txt')


def russian(colors, N, M):
    # 정답 입력 변수
    answer = 0
    # N 행의 개수, M 열의 개수
    now_min = N * M
    # 첫번째 줄은 W 고정, 마지막 줄은 R 고정
    # 그 사이에 들어갈 색깔을 정해야 한다.
    # 순서는 W -> B -> R 로 꼭 고정해야 되고 , B가 꼭 추가

    # 맨 윗줄 흰색으로 변경
    for color in colors[0]:
        if not color == 'W':
            answer += 1
    # 맨 아랫줄 빨강으로 변경
    for color in colors[-1]:
        if not color == 'R':
            answer += 1
    # 그 사이에 들어갈 색깔 결정
    # W, B, R
    need_change = [[M, M, M] for _ in range(N)]
    # 각 행마다 통일 시킬 때 필요한 색깔의 개수룰 구한다
    for i in range(1, N-1):
        for color in colors[i]:
            if color == 'W':
                need_change[i][0] -= 1
            elif color == 'B':
                need_change[i][1] -= 1
            else:
                need_change[i][2] -= 1
    # 밑의 반복문에서 answer를 초기화 하기 위 한 값을 만든다.
    change_answer = []
    change = answer
    # 파랑색이 몇개 들어가고 다른 색깔이 몇개 들어갈지를 결정하자
    # 1. 파랑색을 한개씩 증가시킨다
    # i 파랑색의 개수
    for i in range(1, N - 1):
        # b 파랑색이 시작하는 위치
        for b in range(1, N-i):
            # 파랑색으로 바꾸는데 필요한 값을 구한다.
            for j in range(b, b+i):
                answer += need_change[j][1]
            # 흰색으로 바꾸는 데 필요한 개수
            for w in range(1, b):
                answer += need_change[w][0]
            # 빨강색을 바꾸는 데 필요한 개수
            for r in range(b+i, N-1):
                answer += need_change[r][2]
            # 주어진 값이 더 작은지 확인
            change_answer.append(answer)
            answer = change
    return min(change_answer)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    flags = []
    for _ in range(N):
        flags.append(list(map(str, input())))
    print('#{} {}'.format(t, russian(flags, N, M)))