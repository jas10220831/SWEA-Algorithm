import sys
sys.stdin = open('input.txt')


def prize(number, N):
    check = set([number])
    check2 = set()

    for _ in range(N):
        while check:
            # 숫자 하나 뺴고 리스트 형태로 변환
            numb = list(str(check.pop()))
            for i in range(len(numb)-1):
                for j in range(i+1, len(numb)):
                    numb[i], numb[j] = numb[j], numb[i]
                    # 자리를 바꾸고 다시 숫자로 바꾼다.
                    # 스택을 하나만 쓰면 무한루프에 빠진다.
                    # 새로운 스택에 넣자.
                    check2.add(int(''.join(numb)))
                    # 추가하고 자리 원상복구해서 새로운 패턴 확인
                    numb[i], numb[j] = numb[j], numb[i]
        # 루프 한번 다 돌았으면  스택 서로 교체
        check, check2 = check2, check
    return max(check)


T = int(input())
for t in range(1, T+1):
    number, N = map(int, input().split())
    answer = 0
    print('#{} {}'.format(t, prize(number, N)))
