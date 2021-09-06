import sys
sys.stdin = open('sample_input.txt')


def tree1(roots):
    # 루트 1/1
    a = 1
    b = 1
    for root in roots:
        if root == 'L':
            a = a
            b = a + b

        else:
            a = a + b
            b = b
    return [a, b]

T = int(input())
for t in range(1, T+1):
    roots = list(map(str, input()))
    print('#{}'.format(t), *tree1(roots))