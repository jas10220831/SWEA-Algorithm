import sys
sys.stdin = open('input.txt')


def count_date(month1, day1, month2, day2):
    # 각 월별 날 수를 따로 저장해 놓고 필요한 값을 꺼내서 계산하도록한다.
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 월을 idx로 사용해서 날짜를 계산한다.
    count = 0
    for i in range(month1, month2+1):
        # 각 월별 날짜 - day1 - (month2 day - day2) +1
        count += days[i]
    count -= (day1 + (days[month2] - day2) - 1)
    return count

T = int(input())

for t in range(1, T+1):
    month1, day1, month2, day2 = map(int, input().split())
    print('#{} {}'.format(t, count_date(month1, day1, month2, day2)))