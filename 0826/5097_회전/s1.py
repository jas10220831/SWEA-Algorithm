import sys
sys.stdin = open('sample_input.txt')


# idx를 써서 풀 수 있도록 하자
def rotate(numb_len, rotate_count, numbers):
    for _ in range(rotate_count):
        # deque 실행
        move_number = numbers[0]
        # 뒤에 있는 값들을 앞으로 한칸 옮긴다.
        numbers[:numb_len] = numbers[1:]
        # enque 실행
        # 맨 뒤에 뽑아낸 숫자를 넣는다.
        numbers.append(move_number)
    return numbers[0]


T = int(input())
for t in range(1, T+1):
    numb_len, rotate_count = map(int, input().split())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(t, rotate(numb_len, rotate_count, numbers)))
