import sys
sys.stdin = open('sample_input.txt')


def pizza(size, pizzas):
    hwaduk = []
    for _ in range(size):
        # 넣을 때부터 치즈를 녹이고 시작
        hwaduk.append(pizzas.pop(0))
    while len(hwaduk) > 1:
        now = hwaduk.pop(0)
        now[1] = now[1] // 2
        if now[1]:
            hwaduk.append(now)
        else:
            if len(pizzas):
                hwaduk.append(pizzas.pop(0))
    return hwaduk[0][0]





T = int(input())
for t in range(1, T+1):
    size, pizza_count = map(int, input().split())
    cheeses = list(map(int, input().split()))
    pizzas = []
    for i, cheese in enumerate(cheeses):
        pizzas.append([i+1, cheese])
    print('#{} {}'.format(t, pizza(size, pizzas)))