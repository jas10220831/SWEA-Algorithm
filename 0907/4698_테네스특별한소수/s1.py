import sys
sys.stdin = open('sample_input.txt')


def check_D(number, D):
    while number:
        if number % 10 == D:
            return True
        number = number // 10
    return False


def answer(D, start_numb, end_numb):
    answer = 0
    # 에라토스테네스의 채
    checks = [1] * (10 ** 6 + 1)
    checks[0] = 0
    checks[1] = 0

    for number, check in enumerate(checks):
        if check:
            idx = 2
            while number * idx <= 10 ** 6:
                checks[number * idx] = 0
                idx += 1

    for i in range(start_numb, end_numb+1):
        if checks[i] and check_D(i, D):
            answer += 1

    return answer

T = int(input())
for t in range(1, T+1):
    D, start, end = map(int, input().split())
    print('#{} {}'.format(t, answer(D, start, end)))
