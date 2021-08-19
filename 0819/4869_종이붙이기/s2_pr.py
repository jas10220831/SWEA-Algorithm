import sys
sys.stdin = open('sample_input.txt')

memo_stack = [0, 1, 3]


def stack(n):
		# memo_stack의 길이가 n 이하일 경우, stack(n) 값이 리스트에 없으므로, 추가 필요
    if n > 2 and len(memo_stack) <= n:
        memo_stack.append(stack(n - 1) + 2 * stack(n - 2))
    return memo_stack[n]


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())    # 바닥 직사각형 가로 길이
    n = N // 10

    print('#{}'.format(test_case), stack(n))