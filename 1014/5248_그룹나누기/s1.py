import sys
sys.stdin = open('sample_input.txt')



def find_set(x):
    if x == ls[x]:
        return x
    else:
        return find_set(ls[x])

def union(x, y):
    ls[find_set(y)] = find_set(x)


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    memo = list(map(int, input().split()))
    ls = list(range(N+1))
    for i in range(M):
        union(memo[2*i], memo[2*i+1])
    for i in range(N+1):
        if find_set(i) != ls[i]:
            ls[i] = find_set(i)
    print('#{} {}'.format(t, len(set(ls))-1))