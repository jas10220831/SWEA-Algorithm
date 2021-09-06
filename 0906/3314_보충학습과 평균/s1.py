import sys
sys.stdin = open('sample_input.txt')


def answer(scores):
    answer = 0
    for score in scores:
        if score < 40:
            answer += 40
        else:
            answer += score
    return int(answer/5)


T = int(input())
for t in range(1, T+1):
    scores = list(map(int, input().split()))
    print('#{} {}'.format(t, answer(scores)))