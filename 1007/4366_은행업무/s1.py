import sys
sys.stdin = open('sample_input.txt')


def find(numb1, numb2):
    for i in range(len(numb1) - 1):
        temp = numb1[:]
        # 2진수의 자릿수 변경해보기
        temp[i] = str(((int(temp[i]) + 1) % 2))
        # 2진수 10진수로 변경
        change = int(''.join(temp), 2)
        # 3진수 숫자를 변경해 가면서 비교하기
        for j in range(len(numb2)-1):
            # 1, 2를 한번씩 더하고 3의 나머지를 통하여 값을 비교
            for k in range(1, 3):
                temp2 = numb2[:]
                # j 번쨰 자릿수 변경
                temp2[j] = str((int(temp2[j]) + k) % 3)
                # 3진수 숫자 10진수로 변경
                change2 = int(''.join(temp2), 3)
                if change == change2:
                    return change

T = int(input())
for t in range(1, T+1):
    # 값을 바꾸기 편하게 리스트로 받는다.
    numb1 = list(input())
    numb2 = list(input())
    print('#{} {}'.format(t, find(numb1, numb2)))
