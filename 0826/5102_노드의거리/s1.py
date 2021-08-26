import sys
sys.stdin = open('sample_input.txt')


def find_min(node,line, roads, start, end):
    # 방문표시를 한다.
    visited = [0] * (node+1)
    queue = [start]
    while queue:
        now = queue.pop(0)
        if now == end:
            return visited[now]
        # 현재 위치에 해당하는 행에서 연결된 노드를 찾는다.
        for idx, x in enumerate(roads[now]):
            # 방문하지 않았고, 길이 존재하는 경우
            if x and not visited[idx]:
                # 해당 위치를 추가한다.
                queue.append(idx)
                visited[idx] = visited[now] + 1
    # 연결되어 있지 않는 경우 꼭 넣어주자!
    return 0


T = int(input())
for t in range(1, T+1):
    node, line = map(int, input().split())
    roads = [[0] * (node + 1) for _ in range(node + 1)]
    for _ in range(line):
        y, x = map(int, input().split())
        # 양방향 통행이 가능하므로 역방향에도 1추가
        roads[y][x] = 1
        roads[x][y] = 1
    start, end = map(int, input().split())
    print('#{} {}'.format(t, find_min(node, line, roads, start, end)))