import sys
sys.stdin = open('s_input.txt')


def find_set(numb):
    if numb == group[numb]:
        return numb
    else:
        return find_set(group[numb])


def union(x, y):
    group[find_set(y)] = find_set(x)



T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    group = list(range(0, N+1))
    for _ in range(M):
        x, y = map(int, input().split())
        union(x, y)
    for i in range(N+1):
        if not group[i] == find_set(i):
            group[i] = find_set(i)


    print('#{} {}'.format(t, len(set(group[1:]))))