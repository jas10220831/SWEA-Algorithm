import sys
sys.stdin = open('input.txt')


def answer(crops, size):
    # 수확할 위치 시작
    check = size//2
    # 수확 개수 정하기
    idx = 0
    answer = 0
    i = 0
    while i < size:
        answer += sum(crops[i][check:check+idx+1])
        # 중앙보다 위일 경우 한칸 뒤로
        if i < size//2:
            # 수확 시작할 idx
            check -= 1
            idx += 2
        else:
            check += 1
            idx -= 2
        i += 1
    return answer



T = int(input())
for t in range(1, T+1):
    size = int(input())
    crops = []
    for _ in range(size):
        crops.append(list(map(int, input())))
    print('#{} {}'.format(t, answer(crops, size)))