import sys
sys.stdin = open('input.txt')
while True:
    try:
        # N : 케이스 번호
        N = int(input())
        ladder = [[0] for _ in range(100)]
        ladder_size = 100
        i, j = 0, 0
        # 움직임 제어 : 0->하, 1->좌, 2->우
        direction = 0

        # Target X 에서 출발 할 수 있도록 배열의 열 역순 정렬
        for input_index in range(ladder_size-1, -1, -1):
            ladder[input_index] = list(map(int, input().split()))
            if 2 in ladder[input_index]:
                j = ladder[input_index].index(2)

        while i < ladder_size:
            # 좌로 움직임
            if (direction == 0 or direction == 1) and j-1 >= 0 and ladder[i][j-1] == 1:
                i += 0
                j -= 1
                direction = 1
            # 우로 움직임
            elif (direction == 0 or direction == 2) and j+1 <= ladder_size-1 and ladder[i][j+1] == 1:
                i += 0
                j += 1
                direction = 2
            # 하로 움직임
            else:
                i += 1
                j += 0
                direction = 0

        print("#{0} {1}".format(N, j))
    except EOFError:
        break