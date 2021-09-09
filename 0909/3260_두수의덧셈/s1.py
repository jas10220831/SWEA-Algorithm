T = int(input())
for t in range(1, T+1):
    numb1, numb2 = map(int, input().split())
    print('#{} {}'.format(t, numb1+numb2))