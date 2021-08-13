import sys
sys.stdin = open('input.txt')

T = int(input())


def water_cost(P, Q, R, S, W):
    a_cost = P * W
    if W <= R:
        b_cost = Q
    else:
        b_cost = Q + (W - R) * S
    if a_cost > b_cost:
        return b_cost
    else:
        return a_cost

for t in range(1, T+1):
    P, Q, R, S, W = map(int,input().split())
    print('#{} {}'.format(t, water_cost(P, Q, R, S, W)))
