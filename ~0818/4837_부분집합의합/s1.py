import sys
sys.stdin = open('sample_input.txt')

# 테스트 케이스의 수
T = int(input())

for t in range(1, T+1):
    # 부분집합 원소 개수 N, 찾아야 되는 합의 값 K
    N, K = map(int, input().split())
    # 1~12를 포함한 행렬 생성
    numbers_list = list(range(1, 13))
    len_numbers = len(numbers_list)
    answer = 0
    for i in range(1 << len_numbers):
        # 각 부분집합을 확인할 리스트를 만든다.
        sample_list = []
        for j in range(len_numbers):
            if i & (1 << j):
                sample_list.append(numbers_list[j])
        if len(sample_list) == N and sum(sample_list) == K:
            answer += 1
    print('#{0} {1}'.format(t, answer))


