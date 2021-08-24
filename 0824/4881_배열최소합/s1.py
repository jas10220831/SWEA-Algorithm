import sys
sys.stdin = open('sample_input.txt')


def find_min(y):
    global sum_numb, answer
    # 합이 answer 보다 크면 그냥 멈춘다.
    if sum_numb > answer:
        return
    # 맨 끝에 도달하면 멈추고 합을 비교한다.
    if y == N:
        if sum_numb < answer:
            answer = sum_numb
        return

    # 각 행을 돌며 사용하지 않은 열이면 뽑아서 사용
    for x in range(N):
        if not visited[x]:
            sum_numb += numbers[y][x]
            visited[x] += 1
            # y를 한칸 아래로 내려가고 값을 구한다.
            find_min(y+1)
            # global 변수를 사용하고 있으므로 값을 초기화 해준다.
            visited[x] -= 1
            sum_numb -= numbers[y][x]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    sum_numb = 0
    answer = 9999
    visited = [0] * N
    numbers = []
    for _ in range(N):
        numbers.append(list(map(int, input().split())))
    find_min(0)
    print('#{} {}'.format(t, answer))
