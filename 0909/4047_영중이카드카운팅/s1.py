import sys
sys.stdin = open('sample_input.txt')


def card_counting(cards):
    counting = {
        'S': [0]+([1] * 13),
        'D': [0]+([1] * 13),
        'H': [0]+([1] * 13),
        'C': [0]+([1] * 13)
    }
    for i in range(0, len(cards), 3):
        idx = int(cards[i+1:i+3])
        counting[cards[i]][idx] -= 1
        if counting[cards[i]][idx] < 0:
            return ['ERROR']

    answer = [sum(counting['S']), sum(counting['D']), sum(counting['H']), sum(counting['C'])]
    return answer


T = int(input())
for t in range(1, T+1):
    cards = str(input())
    print('#{}'.format(t), *card_counting(cards))