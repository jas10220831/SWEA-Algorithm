import sys
sys.stdin = open('sample_input.txt')


def tape(length):
    if length == 10:
        return 1
    elif length == 20:
        return 3
    else:
        return tape(length - 10) + 2 * tape(length - 20)


T = int(input())
for t in range(1, T+1):
    length = int(input())
    print('#{} {}'.format(t, tape(length)))
