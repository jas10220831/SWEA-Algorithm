import sys
sys.stdin = open('sample_input.txt')


def check(strings):
    check_list = []
    # 닫는 괄호가 더 많을 경우 인덱스 에러 발생
    try:
        for word in strings:
            if word == '{' or word == '(':
                check_list.append(word)
            elif word == '}':
                if check_list.pop() == '{':
                    continue
                else:
                    return 0
                    break
            elif word == ')':
                if check_list.pop() == '(':
                    continue
                else:
                    return 0
                    break
            else:
                continue
    except:
        return 0
    if len(check_list):
        return 0
    else:
        return 1


T = int(input())
for t in range(1, T+1):
    strings = input()
    print('#{} {}'.format(t, check(strings)))
