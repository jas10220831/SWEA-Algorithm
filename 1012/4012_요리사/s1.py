import sys
sys.stdin = open('sample_input.txt')

import itertools


def cooking(numbers):
    global answer

    # nCn/2의 조합들
    ing = list(itertools.combinations(range(0, N), int(N/2)))

    # 각 재료들을 분배
    for ing1 in ing:
        ing2 = []
        for i in range(0, N):
            if i not in ing1:
                ing2.append(i)
        # nP2로 재료 나누고 시너지 계산
        ing1_per = list(itertools.permutations(ing1, 2))
        ing2_per = list(itertools.permutations(ing2, 2))
        synergy1 = 0
        synergy2 = 0
        for food in ing1_per:
            synergy1 += numbers[food[0]][food[1]]
        for food in ing2_per:
            synergy2 += numbers[food[0]][food[1]]
        if answer > abs(synergy1 - synergy2):
            answer = abs(synergy1 - synergy2)



T = int(input())
for t in range(1, T+1):
    N = int(input())
    foods = [list(map(int, input().split())) for _ in range(N)]
    answer = 20000 * 20000
    cooking(foods)
    print('#{} {}'.format(t, answer))