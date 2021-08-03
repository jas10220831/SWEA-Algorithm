T = int(input())

for t in range(1, T+1):
    #N은 가로,세로 길이 K는 글자의 길이
    N, K = map(int,input().split())

    answer = 0
    blanks = []
    for _ in range(N):
        blanks.append(list(map(str, input().split())))
    
    #가로 세로로 검색한다. 
    #팔요한 빈칸의 개수 
    #padding 한다. 매트릭스 사변에 0추가
    # '0 1*K 0'을 count
    ch_word = '0' + '1' * K + '0'

    #padding한 matrix 작성
    blanks.insert(0, (['0'] * N))
    blanks.append(['0'] * N)
    #각 행 앞뒤로 '0'추가
    for blank in blanks:
        blank.insert(0, '0')
        blank.append('0')
    

    #세로탐색을 먼저 고정
    for height in blanks:
        #가로 탬색 시작
        w_blank = ''
        for b in height:
            #ex) k=3 , '111'이 해당 열에 포함됐는지 확인 and ``
            w_blank += b
        #w_blank의 값을 슬라이싱하여 값을 비교한 다음 더한다. 
            for i in range(0,N-K):
                print(w_blank[i : i+K+2])
                # if w_blank[i : i+K+1] == ch_word:
                #     answer += 1
            
        

    #가로 고정 
    for width in range(N+2):
        h_blank = ''
        for height in range(N+2):
            h_blank += blanks[height][width]
            for i in range(0,N-K):
                if h_blank[i : i+K+2] == ch_word:
                    answer += 1

    print(f'#{t} {answer}')
