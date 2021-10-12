import sys
sys.stdin = open('sample_input.txt')

def answer(barcodes):
    # 중복되는 문자열을 모두 삭제
    barcodes = list(set(barcodes))

    #16진수를 4자리수 2진수로 변경
    def change(number):
        answer = ''
        for i in number:
            # 비트 연산을 통해서 값을 구성
            for j in range(3, -1, -1):
                # int(literal, base) literal을 base진수 기준으로 10진수로 변환
                answer += '1' if int(i, 16) & (1 << j) else '0'
        return answer

    # 암호문들을 저장할 리스트
    passwords = []
    # 16진수의 숫자들을 찾아내기
    for i in range(len(barcodes)):
        # 16진수를 저장할 변수
        # 암호문은 0부터 시작
        for j in range(len(barcodes[i])):
            # 암호문 시작
            # 16진수를 4bit 2진수로 변경
            if barcodes[i][j] != '0':
                # 맨뒤가 0으로 끝나도 상관은 없다. 이진수로 바꾼 뒤 암호문의 맨 끝은 1이다.
                passwords.append(barcodes[i][j:])
                # 암호문이 하나가 아닐 수도 있다.
                break

    # 코드 해석 과정
    def decoding(code):
        # 해독을 위한 과정
        decodes = {
            '211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5,\
            '114': 6, '312': 7, '213': 8, '112': 9
        }
        # 비율 확인을 위해 1, 0 변화 확인 3이면 숫자 하나 입력 비율 확인
        ratio = [0, 0, 0]
        # 해독한 숫자를 추가
        decode_numbers = []
        for i in range(len(code)-1, -1, -1):
            check = 0
            # 맨 앞의 2개가 없으면서 맨 뒤의 '1'일 경우
            if not ratio[0] and not ratio[1] and code[i] == '1':
                # 맨뒤
                ratio[2] += 1
            # 앞의 1개 0 & 맨뒤 값있고 code가 0
            elif not ratio[0] and ratio[2] and code[i] == '0':
                ratio[1] += 1
            # 뒤 값2개 값있고 code 1
            elif ratio[1] and ratio[2] and code[i] == '1':
                ratio[0] += 1
            # 모든 값들이 카운팅 됐고 앞의 code가 0인 경우
            # 또는 맨 앞자리로 도착했을 경우
            if all(ratio) and code[i] == '0' or i == 0:
                # 가로가 56보다 큰 경우 최소값으로 나눠준다
                min_numb = min(ratio)
                if min_numb > 1:
                    for i in range(3):
                        ratio[i] = int(ratio[i] / min_numb)
                decode = ''.join(map(str, ratio))
                # 숫자는 역순으로 저장된다! 이를 꼭 명심!
                # 마지막 인덱스에 도착했지만 의미없는 경우 제외
                if decode != '000':
                    decode_numbers.append(decodes[decode])
                # print('ratio', ratio)
                # print('decode', decodes[decode])
                ratio = [0, 0, 0]
        return decode_numbers



    # # 해독된 전체 암호의 모음
    numbers = []
    for now in passwords:
        code = change(now)
        # 변환으로 받은 숫자들
        # 변환으로 받은 숫자들
        numbs = decoding(code)
        numbers.extend(numbs)

    new_numbers = []
    for i in range(0, len(numbers), 8):
        if not numbers[i: i+8] in new_numbers:
            new_numbers.append(numbers[i: i+8])
    answer = 0
    for nums in new_numbers:
        check = 0
        for idx, num in enumerate(nums):
            if idx % 2:
                check += (3 * num)
            else:
                check += num
        if not check % 10:
            answer += sum(nums)

    return answer

T = int(input())
for t in range(1, T+1):
    # N, 세로의 길이, M 가로의 길이
    N, M = map(int, input().split())
    barcodes = [input().strip().rstrip('0') for _ in range(N)]
    print('#{} {}'.format(t, answer(barcodes)))


