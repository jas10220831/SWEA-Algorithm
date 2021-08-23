import sys
sys.stdin = open('input.txt')

def pow_number(number, M):
    # 기저값을 설정
    if M == 0 or number == 0:
        return 1
    # 홀수일 경우
    if M % 2 :
        new_pow = pow(number, (M-1)/2)
        return (new_pow * new_pow) * number
    else:
        new_pow = pow(number, M/2)
        return new_pow * new_pow


for t in range(1, 11):
    t = int(input())
    number, M = map(int, input().split())
    print('#{} {}'.format(t, int(pow_number(number, M))))