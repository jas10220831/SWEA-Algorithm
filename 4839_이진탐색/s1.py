import sys
sys.stdin = open('sample_input.txt')

T = int(input())
def binary_search(page, search):
    # 몇번만에 찾았는지 푯;
    count = 0
    left = 1
    right = page
    while True:
        center = int((left + right) / 2)
        # 탐색하지 못했을 경우
        if left > right:
            return -1
            break
        if search == center:
            break
        else:
            if search > center:
                left = center
            else:
                right = center
        count += 1
    return count
for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    count_Pa = binary_search(P, Pa)
    count_Pb = binary_search(P, Pb)
    if count_Pa < count_Pb:
        answer = 'A'
    elif count_Pa > count_Pb:
        answer = 'B'
    else:
        answer = 0
    print('#{0} {1}'.format(t, answer))

