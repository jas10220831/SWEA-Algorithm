import sys
sys.stdin = open('input.txt')


def bread(M, K, guests):
    '''
    :param N: 손님의 수
    :param M: 붕어빵 완성되는 시간
    :param K: 만들어지는 붕어빵 개수
    :param guests: 손님들 도착 시간
    :return:
    '''
    # 현재 붕어빵의 개수
    bread = 0
    # 일단 손님들 도착 시간을 오름차순으로 정리해서 queue를 쓰자
    guests = sorted(guests)
    answer = 'Possible'
    # 시작시간을 0으로 하면 무조건 처음에 붕어빵이 구워진다.
    time1 = 1
    while guests:
        time2 = guests.pop(0)
        # stack으로 풀자
        # time에 1을 더하지 않으면 같은 시간대에 여러명의 손님이 오면 중복으로 빵이 추가된다.
        # 다음 시간대에 손님이 오더라도 어차피 1초를 더해줘야 한다.
        for i in range(time1+1, time2+1):
            # 빵이 만들어지는 시간이 된다면
            # i 가 M의 배수라면?
            if i % M == 0:
                # 만들어지는 빵을 추가한다.
                bread += K
        # 손님이 도착, 붕어빵 하나 추가
        bread -= 1
        # 다음 손님이 오는 시간을 입력한다.
        time1 = time2
        if bread < 0:
            answer = 'Impossible'
            break
            return answer
    return answer


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    guests = list(map(int, input().split()))
    print('#{} {}'.format(t, bread(M, K, guests)))