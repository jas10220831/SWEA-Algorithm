T = int(input())
for t in range(1, T+1):
    N = int(input())
    juice = '1/{}'.format(N)
    answer = [juice] * N
    print('#{}'.format(t), end=' ')
    print(*answer)