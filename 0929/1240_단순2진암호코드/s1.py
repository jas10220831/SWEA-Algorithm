import sys
sys.stdin = open('input.txt')


def password(barcode, N, M):
    # 암호문을 뽑기 위해서 탐색 시작
    # 모든 암호는 1로 끝난다. 뒤에서 부터 1을 찾고 앞으로 56칸을 따로 뽑아서 암호문으로 저장
    for i in range(N):
        for j in range(M-1, -1, -1):
            if barcode[i][j] == '1':
                secret = barcode[i][j-55: j+1]
                break

    # 암호문을 뽑아 냈다.
    # 해독문을 dictionary 형태로 저장
    decode = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,\
              '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    # 암호문에서 7글자씩 잘라서 숫자들을 저장
    decoding = []
    for i in range(0, 56, 7):
        word = secret[i: i+7]
        decoding.append(decode[word])
    # 암호문인지 확인하는 과정
    check = 0
    # 홀수자리 *3, 짝수, 검증코드 +
    for idx, number in enumerate(decoding):
        # 홀수일 경우
        if (idx + 1) % 2:
            check += (3 * number)
        # 짝수 & 검증코드
        else:
            check += number
    # 올바른 암호문인지 확인
    if not check % 10:
        return sum(decoding)
    else:
        return 0


T = int(input())
for t in range(1, T+1):
    # 배열의 세로 크기 N(1<= N <= 50), 가로크기 M(1 <= M <= 100)
    N, M = map(int, input().split())
    barcode = [str(input()) for _ in range(N)]
    # print(barcode)
    print('#{} {}'.format(t, password(barcode, N, M)))

