import sys
sys.stdin = open('sample_input.txt')


def check(number, special):
    while number:
        if number % 10 == special:
            return True
        number = number // 10
    return False


def special_number(numb1, numb2, special):
    answer = 0
    numbers = []
    for number in range(numb1, numb2+1):
        if number == 2 or check(number, special) and number % 2:
            numbers.append(number)
    for number in numbers:
        flag = 1
        for i in range(2, number):
            if number % i == 0:
                flag = 0
                break
        if flag:
            answer += 1
            print(answer)
    return answer


T = int(input())
for t in range(1, T+1):
    special, numb1, numb2 = map(int, input().split())
    print('#{} {}'.format(t, special_number(numb1, numb2, special)))