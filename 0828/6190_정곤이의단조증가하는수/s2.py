import sys
sys.stdin = open('s_input.txt')


# nC2를 통하여 부분집합을 구한다.
# 곱한다
# 단조증가를 확인한다

def check_numbers(N, numbers):
    answer = -1
    # nC2를 실행한다.
    for i in range(N-1):
        for j in range(i+1, N):
            # flag 를 통하여 단조증가하는지 아닌지를 확인하도록 한다.
            flag = 0
            numb1 = numbers[i]
            numb2 = numbers[j]
            # 만들어진 숫자 조합에서 단조 증가를 확인한다.
            new_number = numb1 * numb2
            # 숫자의 각 자리수를 비교한다.
            a = new_number
            check_1 = a % 10
            a = a // 10
            while a:
                # 10의 자리수
                check_2 = a % 10
                a = a // 10
                if check_2 > check_1:
                    # 단조증가 하지 않으므로 -1을 하여 flag를 표시한다.
                    flag = 1
                    break
                check_1 = check_2
            if flag:
                continue
            else:
                if new_number > answer:
                    answer = new_number

    return answer


T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(t, check_numbers(N, numbers)))

