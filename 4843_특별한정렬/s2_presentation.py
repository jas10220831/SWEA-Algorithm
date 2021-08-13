import sys
sys.stdin = open('sample_input.txt')

# 리스트 정렬하기
# 선택 정렬 함수 선언
# 최솟값을 찾아 앞쪽으로 정렬하는 오름차순으로 구성
def select_sorting(numbers):
    for i in range(len(numbers) - 1):
        min_idx = i
        for j in range(i + 1, len(numbers)):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


# 테스트 케이스의 수
T = int(input())
for test_case in range(1, 1+T):
    N = int(input())  # 정수의 개수
    # N개의 정수 리스트
    numbers = list(map(int, input().split()))

    sorted_numbers = select_sorting(numbers)
    # 출력될 값이 들어간 special_list 선언
    special_list = []
    # 10: 출력될 숫자의 개수
    for idx in range(10):
        # idx가 짝수일 경우 큰 값을 역순으로 가짐
        # .pop 을 활용하여 정렬된 리스트의 마지막 값을 special_list 에 추가
        if idx % 2 == 0:
            special_list.append(sorted_numbers.pop())
        # idx가 홀수일 경우 작은 값을 가짐
        # .pop 을 활용하여 정렬된 리스트의 처음 값을 special_list 에 추가
        else:
            special_list.append(sorted_numbers.pop(0))

    print('#{}'.format(test_case), *special_list)