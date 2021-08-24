import sys
sys.stdin = open('input.txt')


def caculater(elements):
    # 저장할 스택을 생성
    stack = []
    # 후위식을 저장할 리스트 생성
    post = []
    # 연산자를 저장할 dict 생성
    icp = {'(':3, '+':1, '*' :2, ')': -1}
    isp = {'(': 0, '+': 1, '*': 2, ')': -1}

    for element in elements:
        # 숫자일 경우 후위식에 바로 추가
        if element.isdigit():
            post.append(int(element))
        else:
            if element == '(' or icp[element] > isp[stack[-1]]:
                stack.append(element)
            elif element == ')':
                while stack[-1] != '(':
                    post.append(stack.pop())
                stack.pop()
            else:
                while icp[element] < isp[stack[-1]]:
                    post.append(stack.pop())
                stack.append(element)

    # 계산하기
    for number in post:
        if type(number) == int:
            stack.append(int(number))
        else:
            n1 = stack.pop()
            n2 = stack.pop()
            if number == '+':
                stack.append(n2 + n1)
            else:
                stack.append(n2 * n1)
    return stack.pop()


for t in range(1, 11):
    N = int(input())
    elements = input()
    print('#{} {}'.format(t, caculater(elements)))