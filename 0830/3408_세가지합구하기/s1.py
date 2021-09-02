import sys
sys.stdin = open('sample_input.txt')


def three_sum(N):
    answer = [0, 0, 0]
    for i in range(1, N+1):
        answer[0] += i
        answer[1] += ((2 * i) -1)
        answer[2] += 2 * i

    return answer
# 시간초과가 나온다.
# 리스트로 앞의 결과값을 저장하고 그다음에는 다음 값만 하나씩 더해나가는 식으로 해야될듯?

T = int(input())
for t in range(1, T+1):
    N = int(input())
    print('#{}'.format(t), end=' ')
    print(*three_sum(N))