import sys
sys.stdin = open('input.txt')


def magnetic(matrix):
    '''
    N극을 기준으로만 생각한다.
    N극이 있는 위치 기준으로 밑에 S극(2)가 하나라도 있으면
    count += 1
    :param matrix: 자석들의 위치
    :return:
    '''
    # N극의 위치들을 저장
    n_idx = []
    # 행의 위치
    for i in range(100):
        for j in range(100):
            # 해당 위치가 N극일 경우
            if matrix[i][j] == 1:
                n_idx.append([i, j])
    return n_idx


def check(idx, matrix):
    for i in range(idx[0]+1, 100):
        # 같은 극인 N극을 만나게 된다면 밑에 S극이 있어도
        # 하나의 교착상태가 된다. 그러므로 뺀다.
        if matrix[i][idx[1]] == 1:
            return 0
        # 다른 N극이 없는 상태에서 S극 만나면 바로 교착상태
        elif matrix[i][idx[1]] == 2:
            return 1
    # 아무일 없으면 그냥 0
    return 0


def find(matrix):
    answer = 0
    n_idx = magnetic(matrix)
    for idx in n_idx:
        answer += check(idx, matrix)
    return answer


for t in range(1, 11):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    print('#{} {}'.format(t, find(matrix)))