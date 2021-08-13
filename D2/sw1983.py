T = int(input())

#N 학생수, K 알고 싶은 학생 번호


for t in range(1, T+1):
    scores = []
    total_scores = []
    N, K = map(int, input().split())
    #N번 만큼 학생의 점수를 입력 받는다. 
    for _ in range(N):
        scores.append(list(map(int, input().split())))
    for score in scores:
        total_scores.append(score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2)
            
    #K번째 학생의 점수 
    k_score = total_scores[K-1]
    #총점이 동일한 경우는 없다고 했으므로 정렬하여 등수를 알아본다.
    total_scores.sort(reverse = True)
    #내림차순으로 정렬한 점수에서 K학생의 등수를 알 수 있다.
    rank = total_scores.index(k_score)
    print(rank)
    #조건문을 쓰지 않고 구분하는법 
    #구분 기준의 결과값을 하나의 리스트로 작성
    values = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    #각 기준에는 N/10 만큼의 학생들이 들어가게 된다.
    #등수를 기준수로 나눈뒤 반올림 하면 속하게 될 그룹이 나오게 된다. 
    value = round((rank // (N / 10)))
    value = values[value]
    print(f'#{t} {value}')
