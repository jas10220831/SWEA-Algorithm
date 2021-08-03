#테스트 케이스 수
x = int(input())

for idx in range(1, x+1):
    #입력이 종료되면 끝낸다. 
        max_price = 0
        T = int(input())
        Price = list(map(int, input().split(' ')))
        while True:
            #재귀함수를 이용하자 
            #최대값이 맨 처음으로 오면 멈춘다.
            if len(Price) == 0 :
                max_price += 0
                print(f'#{idx} {max_price}')
                #테스트 케이스에 맞게 횟수를 증가시킨다. 
                x += 1
                break
            else :
                #최대값 위치
                idx_max = Price.index(max(Price))
                #구매할 가격 및 개수
                buy_list = Price[:idx_max]
                max_price += (max(Price) * len(buy_list))  - sum(buy_list)
                Price = Price[idx_max+1: ]

                
