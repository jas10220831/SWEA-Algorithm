import sys
sys.stdin = open('input.txt')


# 숫자가 회문인지 아닌지 확인하는 함수
def pel_number(number):
    str_number = str(number)
    new_number = str_number[::-1]
    if str_number == new_number:
        return True
    else:
        return False

def check(numb1, numb2):
    answer = 0
    for number in range(numb1, numb2+1):
        root_number = number**(1/2)
        # 루트가 존재하는지 아닌지 부터 확인
        if root_number == int(root_number):
            # 팰린드롬 확인
            if pel_number(number) and pel_number(int(root_number)):
                answer += 1
    return answer

T = int(input())
for t in range(1, T+1):
    numb1, numb2 = map(int,input().split())
    print('#{} {}'.format(t, check(numb1, numb2)))
