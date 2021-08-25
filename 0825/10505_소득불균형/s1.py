def count_under(N, revenues):
    count = 0
    mean_people = sum(revenues) / N
    for revenue in revenues:
        if revenue <= mean_people:
            count += 1
    return count


T = int(input())
for t in range(1, T+1):
    N = int(input())
    revenues = list(map(int, input().split()))
    print('#{} {}'.format(t, count_under(N, revenues)))