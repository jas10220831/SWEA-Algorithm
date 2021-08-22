import sys
sys.stdin = open('input.txt')


def bus_stop(buses, number_of_stop):
    stop = [0] * 5001
    answer = []
    for bus in buses:
        for i in range(bus[0], bus[1]+1):
            stop[i] += 1
    for number in number_of_stop:
        answer.append(stop[number])

    return answer



T = int(input())
for t in range(1, T+1):
    buses = []
    stops = []
    N = int(input())
    for _ in range(N):
        buses.append(list(map(int, input().split())))
    P = int(input())
    for _ in range(P):
        stops.append(int(input()))
    print('#{}'.format(t), end = ' ')
    print(*bus_stop(buses, stops))