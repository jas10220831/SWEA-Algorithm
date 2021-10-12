import sys
sys.stdin = open('sample_input.txt')


def min_count(numbers, now=1, charged=0):
    global answer

    # 가지치기
    if charged > answer:
        return

    # 도착 했는지 확인
    if now >= N:
        # charged 가 answer 보다 작은지 확인
        # 맨 마지막 정류소에 도착 후 이동하는데
        charged -= 1
        if charged <= answer:
            answer = charged
        return

    # 현재 위치에서 이동 가능 용량
    battery = numbers[now]

    # 문제에서 배터리 용량은 0보다 크다고 했으므로 이동 불가능은 고려하지 않는다.
    # 현재 위치에서 배터리 충전 후 이동 가능한 정류소에서 모두 출발시킨다.
    # BFS가 맞나?
    for new_now in range(now+1, now + battery + 1):
        min_count(numbers, new_now, charged + 1)





T= int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    N = numbers[0]
    numbers[0] = 0
    answer = N
    min_count(numbers)
    print('#{} {}'.format(t, answer))