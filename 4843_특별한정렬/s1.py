import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    # 정수의 개수 N
    N = int(input())
    # 정렬할 숫자의 개수 M
    M = 10
    # 숫자 입력 리스트
    numbers = list(map(int,input().split()))
    # 정답을 입력할 리스트
    answer_list = [0] * M

    # 숫자들 정렬
    for i in range(len(numbers)-1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    # 정렬 됐다.
    # 짝수번째는 큰수가 홀수번째는 작은수가 들어간다.
    for idx in range(len(answer_list)):
        # 큰수가 들어올 차례
        if not idx % 2:
            # 맨 뒤에서 값을 하나 빼온다
            answer_list[idx] = numbers.pop(-1)
        # 작은수가 들어올 차례
        else:
            # 맨 앞에서 빼온다.
            answer_list[idx] = numbers.pop(0)

    print('#{0}'.format(t), end=' ')
    print(*answer_list)
