import sys
sys.stdin = open('sample_input.txt')


def preorder_traverse(tree, node):
    global answer
    if node:
        # visit
        answer += 1
        # 왼쪽 자식 노드
        preorder_traverse(tree, tree[node][0])
        # 오른쪽 자식 노드
        preorder_traverse(tree, tree[node][1])
    return answer


T = int(input())
for t in range(1, T+1):
    answer = 0
    line, target = map(int, input().split())
    nodes = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(line+2)]
    for i in range(0, len(nodes), 2):
        # 부모 노드의 값 nodes[i]
        # 자식 노드의 값 nodes[i+1]
        # 부모 노드의 첫번째 값이 비어 있으면 자식 노드를 넣는다.
        if not tree[nodes[i]][0]:
            tree[nodes[i]][0] = nodes[i+1]
        else:
            tree[nodes[i]][1] = nodes[i+1]

    print('#{} {}'.format(t, preorder_traverse(tree, target)))