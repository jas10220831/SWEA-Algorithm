import sys
sys.stdin = open('sample_input.txt')


def maze(size, roads):
    # delta 활용
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    # 출발지점을 찾는다.
    for i in range(size):
        for j in range(size):
            if roads[i][j] == 2:
                start = [i, j]
    # BFS를 시작한다.
    # 방문확인
    vistied = [[0] * size for _ in range(size)]
    # Queue 생성
    queue_now = []
    # 시작점 넣기
    queue_now.append(start)
    vistied[start[0]][start[1]] = 1
    while queue_now:
        # BFS 맨 처음 위치를 뽑는다.
        now = queue_now.pop(0)
        # 방문 표시를 한다.
        # 현재 위치에서 갈 수 있는 방향 찾기
        for i in range(4):
            if 0 <= now[0] + dy[i] < size and 0 <= now[1] + dx[i] < size:
                new_y = now[0] + dy[i]
                new_x = now[1] + dx[i]
                if not roads[new_y][new_x] and not vistied[new_y][new_x]:
                    queue_now.append([new_y, new_x])
                    vistied[new_y][new_x] += vistied[now[0]][now[1]] + 1
                elif roads[new_y][new_x] == 3:
                    # 처음 방문했던 곳도 1로 추가하고 진행했으므로 1을 뺴준다.
                    return vistied[now[0]][now[1]]-1
                    break
    return 0


T = int(input())
for t in range(1, T+1):
    size = int(input())
    roads = []
    for _ in range(size):
        roads.append(list(map(int, input())))
    print('#{} {}'.format(t, maze(size, roads)))
