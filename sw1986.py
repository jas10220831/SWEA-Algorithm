T = int(input())

for t in range(1, T+1):
    N = int(input())
    sum_total = 0
    for number in range(1, N+1):
        sum_total += number * ((number % 2) -1) + number * (number % 2)
    print(f'#{t} {sum_total}')