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


def plus_number(N, numbers):
    answer = -1
    nC2_list = []
    # nC2를 실행한다.
    for i in range(1 << N):
        check = []
        for j in range(N):
            if i & (1 << j):
                check.append(numbers[j])
        if len(check) == 2:
            nC2_list.append(check)

    # 만들어진 숫자 조합에서 단조 증가를 확인한다.
    for numb in nC2_list:
        a = numb[0] * numb[1]
        # 곱한 숫자를 정렬한 결과가 a와 일치하면 그대로 둔다.
        # string이 들어갔으므로 list를 다시 하나로 합쳐준다.
        new_a = int(''.join(bubble_sort(list(str(a)))))
        if a == new_a and new_a >= answer:
            answer = new_a
    return answer


T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(t, plus_number(N, numbers)))

