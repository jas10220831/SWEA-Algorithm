
import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    # N은 가로,세로 길이 K는 글자의 길이
    N, K = map(int, input().split())


    blanks_word = []
    for _ in range(N):
        blanks_word.append(list(map(str, input().split())))

    def find_blanks(size, word, blanks):
        answer = 0
        # 가로 세로로 검색한다.
        # 팔요한 빈칸의 개수
        # padding 한다. 매트릭스 사변에 0추가
        # '0 1*K 0'을 count
        ch_word = '0' + '1' * word + '0'

        # padding한 matrix 작성
        blanks.insert(0, (['0'] * size))
        blanks.append(['0'] * size)
        # 각 행 앞뒤로 '0'추가
        for blank in blanks:
            blank.insert(0, '0')
            blank.append('0')
        # 전치 전 행렬을 먼저 탐색
        # 전치 후 탐색하고 break
        for height in blanks:
            # 가로 탬색 시작
            w_blank = ''.join(height)
            # 값 탐색
            for i in range(size-word+1):
                if w_blank[i:i+word+2] == ch_word:
                    answer += 1
        # 전치한 행렬을 탐색한 다음에 멈춘다.

        # 전치하자
        for i in range(size+2):
            for j in range(size+2):
                if i < j:
                    blanks[i][j], blanks[j][i] = blanks[j][i], blanks[i][j]
        for height in blanks:
            # 가로 탬색 시작
            w_blank = ''.join(height)
            # 값 탐색
            for i in range(size-word+1):
                if w_blank[i:i+word+2] == ch_word:
                    answer += 1
        return answer

    print(find_blanks(N, K, blanks_word))
