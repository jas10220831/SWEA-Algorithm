import sys
sys.stdin = open('input.txt')


# 가격이 크면 count += 1, 작아지면 그 값 * count
def max_price(N, prices):
    answer = 0
    max_price = 0
    for i in range(N-1, -1, -1):
        if prices[i] >= max_price:
            max_price = prices[i]
        else:
            answer += (max_price - prices[i])
    return answer



# 테스트 케이스 수
T = int(input())
for t in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    print('#{} {}'.format(t, max_price(N, prices)))