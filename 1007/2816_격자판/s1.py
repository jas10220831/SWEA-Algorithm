import sys
sys.stdin = open('sample_input.txt')


def make_number(numbers):
    new_numbs = set()
    numb = ''

    def move_6(numbers, now):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        # 6번 이동
        for i in range(6):
            for k in range(4):
                pass


    for i in range(4):
        for j in range(4):
            numb += numbers[i][j]
            # TODO 6번 이동
            pass


T = int(input())
for t in range(1, T+1):
    numbers = [list(map(str, input().split())) for _ in range(4)]