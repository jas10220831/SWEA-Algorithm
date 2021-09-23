import sys
sys.stdin = open('sample_input.txt')


def min_heap(tree, target_node):
    # 자식 노드에서 부모 노드 비교
    def check(idx):
        # 부모노드가 존재할 경우
        if idx // 2:
            # 부모 노드가 더 클 경우
            if tree[idx // 2] > tree[idx]:
                # 두 값을 변경
                tree[idx // 2], tree[idx] = tree[idx], tree[idx // 2]
                # 부모 노드로 이동하여 재귀
                check(idx // 2)
    # idx의 값을 어떻게 정할 것인가
    for idx in range(1, target_node + 1):
        check(idx)


    answer = 0
    while target_node > 0:
        target_node = target_node // 2
        answer += tree[target_node]

    return answer

T = int(input())
for t in range(1, T+1):
    target_node = int(input())
    numbers = [0]
    numbers.extend(list(map(int, input().split())))
    print('#{} {}'.format(t, min_heap(numbers, target_node)))
