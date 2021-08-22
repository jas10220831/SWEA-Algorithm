def check(times):
    if times[2] < times[0]:
        return times[0] - times[2]
    elif times[0] <= times[2] <= times[1]:
        return 0
    else:
        return -1

T = int(input())
for t in range(1, T+1):
    times = list(map(int, input().split()))
    print('#{} {}'.format(t, check(times)))

