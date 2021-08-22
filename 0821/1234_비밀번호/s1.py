import sys
sys.stdin = open('input.txt')


def password(numbers_len, numbers):
    stack = []
    for number in numbers:
        if not stack or stack[-1] != number:
            stack.append(number)
        else:
            stack.pop()
    return ''.join(map(str, stack))


for t in range(1, 11):
    numbers_len, numbers = map(str, input().split())
    print('#{} {}'.format(t, password(numbers_len, numbers)))