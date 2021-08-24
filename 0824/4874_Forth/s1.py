import sys
sys.stdin = open('sample_input.txt')


# 1. 일단 숫자만 받는 함수를 만든다.
def change(word):
    try:
        int(word)
        return int(word)
    except:
        return word


# 언제 error가 발생할까?
# 1. 숫자는 2개이상 남았는데 연산자가 없을 경우
# 2. 연산자는 남았는데 숫자가 없을 경우

def cacul(numbers):
    # 빈 스택 생성
    stack = []
    for number in numbers:
        # 숫자일 경우
        if type(number) == int:
            stack.append(number)
        # '.'으로 계산을 맞칠 경우
        elif number == '.':
            # 값이 하나만 남아있을 경우 error가 발생하지 않는다.
            if len(stack) == 1:
                answer = stack.pop()
            else:
                answer = 'error'
        # 연산자일 경우
        else:
            # 연산자는 있는데 숫자가 부족하게 남아있으면 error가 발생한다.
            if not len(stack) == 1:
                # 숫자 2개를 꺼낸다.
                numb1 = stack.pop()
                numb2 = stack.pop()
                if number == '+':
                    stack.append(int(numb2 + numb1))
                elif number == '*':
                    stack.append(int(numb2 * numb1))
                elif number == '/':
                    stack.append(int(numb2 / numb1))
                elif number == '-':
                    stack.append(int(numb2 - numb1))
            # 숫자가 한개만 남아 있을 경우 error가 발생한다.
            else:
                # return 값에 error를 넣어주고 반복문을 멈춘다.
                answer = 'error'
                break
    return answer


T = int(input())
for t in range(1, T+1):
    numbers = list(map(change, input().split()))
    print('#{} {}'.format(t, cacul(numbers)))