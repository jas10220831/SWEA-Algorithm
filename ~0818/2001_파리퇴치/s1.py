import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    # 행렬 크기 N, 파리채 크기 M
    N, M = map(int, input().split())
    # 파리 저장할 행렬
    flies = []
    max_flies = -1
    for _ in range(N):
        flies.append(list(map(int, input().split())))

    for height in range(0,N-M+1):
        for width in range(0,N-M+1):
            fly = 0
            for idx in range(M):
                fly += sum(flies[height+idx][width:width+M])
            if max_flies < fly :
                max_flies = fly
    print('#{} {}'.format(t, max_flies))