import sys
sys.stdin = open('sample_input.txt')

# 테스트 케이스 수 입력
T = int(input())

for t in range(1, T+1):
    # 색칠 역역을 0행렬로 표현
    area = [[0] * 10 for _ in range(10)]
    # 칠할 영역의 개수
    N = int(input())
    # N번 만큼 색칠 영역을 받고 칠한다음 다음 케이스로 넘어간다.
    for n in range(N):
        area_list = list(map(int, input().split()))
        area_color = area_list.pop(-1)
        # 색칠을 시작한다.
        # [2, 2, 4, 4]
        # [x1, y1, x2, y2]
        for x in range(area_list[0], area_list[2]+1):
            for y in range(area_list[1], area_list[3]+1):
                # area[x][y]
                # 현재 색칠 된 색깔에 관계없이 추가로 칠한다.
                # 문제에서 같은 색은 겹치지 않는다고 했으므로 따로 고려하지 않는다.
                area[x][y] += area_color
    # 칠해진 행렬에서 3을 찾으면 겹쳐서 칠해지게 된다.
    # 카운팅 정렬 사용
    counting_list = [0] * 4
    # colors = [0,1,2,3, ]
    for colors in area:
        # color = 0,1,2,3
        for color in colors:
            counting_list[color] += 1
    print('#{0} {1}'.format(t, counting_list[3]))