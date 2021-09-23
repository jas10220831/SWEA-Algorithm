import sys
sys.stdin = open('sample_input.txt')


def make_tree(idx):
    if idx < N:
        # 후위 순환으로 값을 계산
        make_tree(idx * 2)
        make_tree(idx * 2 + 1)
        # 루트 노드의 경우 자식 노드 값을 더한다.
        if not tree[idx]:
            # 값이 존재할 경우에만 덧셈 실행
            if idx * 2 <= N:
                tree[idx] += tree[idx * 2]
            if idx * 2 + 1 <= N:
                tree[idx] += tree[idx * 2 + 1]



T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value
    make_tree(1)
    print('#{} {}'.format(t, tree[L]))