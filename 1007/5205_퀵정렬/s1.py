import sys
sys.stdin = open('sample_input.txt')


def quick_sort(numbers, l, r):
    def partition(numbers, l, r):
        # 피벗값 맨 왼쪽 값으로 결정
        p = numbers[l]
        i = l
        j = r
        while i <= j:
            while i <= j and numbers[i] <= p: i += 1
            while i <= j and numbers[j] >= p: j -= 1
            if i <= j:
                numbers[i], numbers[j] = numbers[j], numbers[i]
        # 피벗과 마지막 right 값 변경
        # 피벗값을 자신보다 작고 큰 값 사이에 위치하게 한다.
        numbers[l], numbers[j] = numbers[j], numbers[l]
        # 마지막 위치 값을 반환하여 다음 정렬에서 재귀로 사용
        return j

    if l < r:
        s = partition(numbers, l, r)
        quick_sort(numbers, l, s-1)
        quick_sort(numbers, s+1, r)

    return numbers


T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    print('#{} {}'.format(t, quick_sort(numbers,0, N-1)[N//2]))