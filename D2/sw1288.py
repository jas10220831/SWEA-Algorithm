import sys
sys.stdin = open('input.txt')

T = int(input())
# 카운팅 정렬 쓰자

for t in range(1, T+1):
    N = int(input())
    # 더해갈 배수 i
    i = 1
    # 카운팅 리스트
    count_list = [0] * 10
    # 카운트할 숫자를 입력할 리스트
    number_list = []
    # 0이 하나라도 있으면 계속 진행한다.
    while not all(count_list):
        # 입력받은 숫자를 map과 extend를 사용해 각 자릿수의 숫자로 분리한 뒤 추가
        number_list.extend(list(map(int, str(N * i))))
        for number in number_list:
            count_list[number] += 1
        i += 1
    #마지막에 한번더 더해지는 1을 뺀 뒤 N을 곱하면 양의 개수가 된다.
    #문제를 제대로 읽자 몇번째 인지가 아니라 얼마나 셌으면 이다.
    print('#{} {}'.format(t, (i-1)*N))








