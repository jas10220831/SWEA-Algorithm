import sys
sys.stdin = open('sample_input.txt')


# 에라토스테네스의 채
now = 2
check = [1] *(10 ** 6 + 1)






T = int(input())
for t in range(1, T+1):
    D, start, end = map(int, input().split())
    print('#{} {}'.format(t, answer(D, start, end)))
