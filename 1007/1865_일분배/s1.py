import sys
sys.stdin = open('input.txt')


def max_percent(numbers, worker=0, now=1):
    global answer

    # 성공 확률 더 적을 경우
    if answer >= now:
        return

    # 모든 작업이 끝난 경우
    if all(worked):
        if answer < now:
            answer = now
        return

    for i in range(N):
        # 맨 처음 작업의 확률만 따로 계산
        if not worked[i]:
            worked[i] = 1
            max_percent(numbers, worker+1, now * (numbers[worker][i]))
            worked[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    percent = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    answer = 0
    worked = [0] * N
    max_percent(percent)
    print('#{} {:.6f}'.format(t, answer * 100))



