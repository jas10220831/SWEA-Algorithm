import sys
sys.stdin = open('sample_input.txt')

# 가위바위보를 통해 승자를 가리는 함수
# 여기에 idx를 넣어서 비교해야 한다.
# 즉 나눌 때 부터 가위바위보 해당이 아니라 idx를 넣어서 나눈뒤
# 가위바위보 할때 해당 값을 넣는다.
def winner(numbers):
    # 가위
    if students[numbers[0]] == 1:
        if students[numbers[1]] == 2:
            return numbers[1]
        else:
            return numbers[0]
    elif students[numbers[0]] == 2:
        if students[numbers[1]] == 3:
            return numbers[1]
        else:
            return numbers[0]
    else:
        if students[numbers[1]] == 1:
            return numbers[1]
        else:
            return numbers[0]


# 참가자를 나누는 함수
def seperate(numbers):
    N = len(numbers)
    # 1명만 남았을 경우 경기가 끝나거나 부전승
    if N == 1:
        return numbers[0]
    elif N == 2:
        return winner(numbers)
    # 2명이 됐을 경우 ->
    # 그 이상일 경우 -> 나눠준다.
    if not N % 2:
        sep1 = numbers[:N//2]
        sep2 = numbers[N//2:]
    else:
        sep1 = numbers[:N//2+1]
        sep2 = numbers[N//2+1:]
    return winner([seperate(sep1), seperate(sep2)])


T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 학생들의 번호
    numbers = list(range(0, N))
    # 가위바위보 낸거
    students = list(map(int, input().split()))
    print('#{} {}'.format(t, seperate(numbers)+1))


