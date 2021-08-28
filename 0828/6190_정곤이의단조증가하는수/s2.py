import sys
sys.stdin = open('s_input.txt')


# nC2를 통하여 부분집합을 구한다.
# 곱한다
# 단조증가를 확인한다
def bubble_sort(number):
    for i in range(len(number)-1, 0, -1):
        for j in range(i):
            if number[j] > number[j+1]:
                number[j], number[j+1] = number[j+1], number[j]
    return number


# 단조증가를 확인하는 함수
def check_numbers(N, numbers):
    answer = -1
    # nC2를 실행한다.
    for i in range(N-1):
        numb1 = numbers[i]
        for j in range(i+1, N):
            numb2 = numbers[j]
    # 만들어진 숫자 조합에서 단조 증가를 확인한다.
            a = numb1 * numb2
            # 숫자의 각 자릿수를 비교해 나간다.
            print(a)
    return


T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(t, check_numbers(N, numbers)))

