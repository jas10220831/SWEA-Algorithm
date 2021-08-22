import sys
sys.stdin = open('sample_input.txt')

def check_stick(sticks):
    open = '('
    close = ')'
    answer = 0
    stack = [sticks[0]]
    for i in range(1, len(sticks)):
        # close 일 경우 탐색 필요 없음
        if sticks[i] == open:
            stack.append(open)
        else:
            if sticks[i-1] == close:
                stack.pop()
                answer += 1
            else:
                stack.pop()
                answer += len(stack)
    return answer


T = int(input())
for t in range(1, T+1):
    sticks = str(input())
    print('#{} {}'.format(t, check_stick(sticks)))
