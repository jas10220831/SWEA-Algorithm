T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))

    numbers.remove(max(numbers))
    numbers.remove(min(numbers))

    new_mean = sum(numbers) / len(numbers)
    new_mean = round(new_mean)
    print(f'#{t} {new_mean}')