import sys
sys.stdin = open('sample_input.txt')


def find_road(roads, N):
    dy = [1, 0, -1, 0]
    dx = [0, -1, 0, 1]
    move = 0
    # 이동경로를 저장할 stack을 만든다.
    stack = []
    #  출발점을 찾고 그 위치를 가져온다.
    for i in range(N):
        for j in range(N):
            if roads[i][j] == 2:
                # 출발점을 찾았다면 그 위치를 stack 에 추가한다.
                stack.append([i, j])
    # 방문 표시를 위한 행렬 만들기
    visited = [[0] * N for _ in range(N)]
    # 출발점을 찾았으므로 움직이기 시작한다.
    while stack:
        # 한칸 씩 이동해보며 이동할 수 있는 곳인지 확인후 stack에 추가
        now = stack.pop()
        for i in range(4):
            if 0 <= now[0] + dy[i] < N and 0 <= now[1] + dx[i] < N:
                new_y = now[0] + dy[i]
                new_x = now[1] + dx[i]
                # 한칸씩 움직였을때 0이면서 미로의 범위 안에 있는 경우 stack에 추가
                if roads[new_y][new_x] == 0 and not visited[new_y][new_x]:
                    # 방문한걸로 만든다.
                    visited[now[0]][now[1]] = 1
                    stack.append([new_y, new_x])
                # 움직인 곳에 2가 있으면 멈춘다.
                elif roads[new_y][new_x] == 3:
                    return 1
                    break

            # 다른 위치도 확인한다.
    # 멈추지 않고 전부 탐색했을 경우 2가 없다.
    return 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    roads = []
    for _ in range(N):
        roads.append(list(map(int, input())))
    print('#{} {}'.format(t, find_road(roads, N)))