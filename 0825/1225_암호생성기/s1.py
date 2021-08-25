import sys
sys.stdin = open('input.txt')


def encoding(numbers):
    # 뺼 값을 지정한다.
    minus_numb = 1
    # 맨 뒤값이 0이니 0이하가 될때까지
    while numbers[-1] > 0:
        # deQueue 한 다음
        # 맞는 값을 뺸다음
        # enQueue를 한다.
        move_number = numbers[0] - minus_numb
        # 새로운 배열을 생성
        numbers = numbers[1:]
        numbers.append(move_number)
        # 뺼값 1추가
        minus_numb += 1
        # 뺼값이 6이 되면 1로 바꿔준다.
        if minus_numb == 6:
            minus_numb = 1
        # 새로 만든 배열로 재귀
    numbers[-1] = 0
    return numbers


for t in range(1, 11):
    T = int(input())
    numbers = list(map(int, input().split()))
    print('#{}'.format(t), end = ' ')
    print(*encoding(numbers))