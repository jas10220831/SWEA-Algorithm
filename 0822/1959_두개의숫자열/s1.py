import sys
sys.stdin = open('input.txt')


def max_cal(len1, len2, numbers1, numbers2):
    # 첫번쨰가 두번쨰보다 긴 경우 짧은 쪽을 옮긴다.
    max_sum = -99999999
    if len1 > len2:
        for i in range(len1 - len2 + 1):
            number_sum = 0
            for idx, number in enumerate(numbers2):
                number_sum += (number * numbers1[i + idx])
            if number_sum > max_sum:
                max_sum = number_sum
    else:
        for i in range(len2 - len1 + 1):
            number_sum = 0
            for idx, number in enumerate(numbers1):
                number_sum += (number * numbers2[i + idx])
            if number_sum > max_sum:
                max_sum = number_sum
    return max_sum

T = int(input())

for t in range(1, T+1):
    len1, len2 = map(int, input().split())
    numbers1 = list(map(int, input().split()))
    numbers2 = list(map(int, input().split()))
    print('#{} {}'.format(t, max_cal(len1, len2, numbers1, numbers2)))