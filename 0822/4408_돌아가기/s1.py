import sys
sys.stdin  = open('sample_input.txt')


def change(number):
    return (int(number)+1) // 2


def min_move(room_number):
    corridor = [0] * 201
    for room in room_number:
        if room[0] > room[1]:
            room[1], room[0] = room[0], room[1]
        for i in range(room[0], room[1]+1):
            corridor[i] += 1
    for i in range(len(corridor)-1,0,-1):
        for j in range(0,i):
            if corridor[j] > corridor[j+1]:
                corridor[j], corridor[j+1] = corridor[j+1], corridor[j]
    return corridor[-1]




T = int(input())
for t in range(1, T+1):
    N = int(input())
    rooms = []
    for _ in range(N):
        rooms.append(list(map(change, input().split())))
    print('#{} {}'.format(t, min_move(rooms)))
