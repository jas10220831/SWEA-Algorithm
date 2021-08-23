import sys
sys.stdin = open('input.txt')


# 읽는 값을 변환 숫자로
def make_int(word):
    try:
        int(word)
        return int(word)
    except:
        return word


def caculater(words):
    # 후위식 만들기
    # icp, isp를 미리 지정해서 만들고 사용하자.
    icp = {')': -1, '*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
    isp = {')': -1, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    # token '('을 미리 넣고 시작하자.
    stack1 = ['(']
    # 닫는 괄호를 맨뒤에 추가하자.
    words.append(')')
    # 후위식변수 생성
    post = []
    while stack1:
        for word in words:
            # 숫자가 아닐경우
            if type(word) != int:
                # push 하는 경우 스택 탑과 비교해서 icp > isp 면 push
                if word == '(' or icp[word] > isp[stack1[-1]]:
                    stack1.append(word)
                # 아닐경우 icp 보다 작은 연산자를 만날 때 까지 pop
                elif word == ')':
                    while stack1[-1] != '(':
                        post.append(stack1.pop())
                    # '('은 그냥 버린다.
                    stack1.pop()
                else:
                    while icp[word] < isp[stack1[-1]]:
                        post.append(stack1.pop())
                    stack1.append(word)
            else:
                post.append(word)

    # 후위식 계산하기
    # stack2가 아니라 post가 빈 리스트가 될때까지 실행해야 된다.
    for word in post:
        if type(word) == int:
            stack1.append(word)
        # 연산자일 경우 숫자를 꺼낸다.
        else:
            n1 = stack1.pop()
            n2 = stack1.pop()
            # n2 연산자 n1 실행
            # 연산자를 if 문을 안쓰고 할수는 없을까?
            # 일단 조건문 써보고 나중에 생각
            if word == '+':
                stack1.append(n2 + n1)
            else:
                stack1.append(n2 * n1)

    return stack1.pop()

for t in range(1, 11):
    N = int(input())
    cacul = list(map(make_int, input()))
    print('#{} {}'.format(t,caculater(cacul)))