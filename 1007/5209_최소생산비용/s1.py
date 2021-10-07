import sys
sys.stdin = open('sample_input.txt')


def min_cost(cost, now_cost=0, now_idx=0):
    global answer

    # 가지치기
    if answer < now_cost:
        return

    # 모든 제품 생산완료
    if all(used):
        # 비용이 더 적을 경우
        if answer >= now_cost:
            answer = now_cost
        return

    for i in range(N):
        # 아직 생산 안한 제품
        if not used[i]:
            temp = cost[now_idx][i]
            used[i] = 1
            min_cost(cost, now_cost + temp, now_idx + 1)
            used[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    answer = 100 * N
    min_cost(cost)
    print('#{} {}'.format(t, answer))