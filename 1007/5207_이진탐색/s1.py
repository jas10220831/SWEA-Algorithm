import sys
sys.stdin = open('sample_input.txt')


# 이진탐색 함수 따로 작성
def binary_search(list_A, low, high, number, check=0):
    if low > high:
        return False
    else:
        # 양 쪽을 번갈아 가면서 검색하는지 확인 필요
        mid = (low + high) // 2
        if list_A[mid] == number:
            return True
        elif list_A[mid] > number:
            if check == 1:
                return False
            else:
                check = 1
                return binary_search(list_A, low, mid-1, number, check)

        else:
            if check == -1:
                return False
            else:
                check = -1
                return binary_search(list_A, mid+1, high, number, check)


def search_count(list_A, list_B):
    answer = 0
    # B에서 숫자 하나씩 확인
    for number in list_B:
        if binary_search(list_A, 0, len(list_A) - 1, number):
            answer += 1
    return answer

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    list_A = sorted(list(map(int, input().split())))
    list_B = list(map(int, input().split()))
    print('#{} {}'.format(t, search_count(list_A, list_B)))