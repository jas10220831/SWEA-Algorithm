import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    # N은 가로,세로 길이 K는 글자의 길이
    N, K = map(int, input().split())

    answer = 0
    blanks = []
    for _ in range(N):
        blanks.append(list(map(str, input().split())))

    # 가로 세로로 검색한다.
    # 팔요한 빈칸의 개수
    # padding 한다. 매트릭스 사변에 0추가
    # '0 1*K 0'을 count
    ch_word = '0' + '1' * K + '0'

    # padding한 matrix 작성
    blanks.insert(0, (['0'] * N))
    blanks.append(['0'] * N)
    # 각 행 앞뒤로 '0'추가
    for blank in blanks:
        blank.insert(0, '0')
        blank.append('0')
    # 세로탐색을 먼저 고정
    for height in blanks:
        # 가로 탬색 시작
        w_blank = ''
        for b in height:
            # ex) k=3 , '01110'이 해당 열에 포함됐는지 확인 and ``
            w_blank += b
        #값 탐색
        for i in range(N-K+1):
            if w_blank[i:i+K+2] == ch_word:
                answer += 1
    # 전치하자
    for i in range(N+2):
        for j in range(N+2):
            if i < j:
                blanks[i][j], blanks[j][i] = blanks[j][i], blanks[i][j]
    # 다시 탐색
    for height in blanks:
        # 가로 탬색 시작
        w_blank = ''
        for b in height:
            # ex) k=3 , '01110'이 해당 열에 포함됐는지 확인 and ``
            w_blank += b
        #값 탐색
        for i in range(N-K+1):
            if w_blank[i:i+K+2] == ch_word:
                answer += 1


    print('#{0} {1}'.format(t, answer))