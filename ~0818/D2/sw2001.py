T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split(' '))
    flies = []
    for _ in range(N):
        flies.append(list(map(int, input().split(' '))))
    print(flies)
    max = 0

    #가로 파리의 합
    #sum(flies[h][w:w+M+1])
    #세로르 더하기 위해서 idx를 통해 M-1까지 간다. 
    #세로 파리의 합
    
    for height in range(0,N-M+1):
        for width in range(0,N-M+1):
            fly = 0
            for idx in range(M):
                fly += sum(flies[height+idx][width:width+M])
            if max < fly :
                max = fly
    print(f'#{t} {max}')