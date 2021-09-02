import sys
sys.stdin = open('sample_input.txt')

def diamond(strings):
    # 가운데 줄 생성
    center = []
    for string in strings:
        center.extend(['#', '.', string, '.'])
    center.append('#')
    center = ''.join(center)
    # 첫번째 마지막쨰
    first_last = ['.']
    for _ in range(len(strings)):
        first_last.extend(list('.#..'))
    first_last = ''.join(first_last)
    second_fourth = ['.']
    for _ in range(len(strings)*2):
        second_fourth.extend(list('#.'))
    second_fourth = ''.join(second_fourth)
    answer = [first_last, second_fourth, center, second_fourth, first_last]
    return answer

T = int(input())
for _ in range(T):
    strings = list(map(str, input()))
    for i in diamond(strings):
        print(i)

