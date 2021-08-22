import sys
sys.stdin = open('sample_input.txt')


def remove(words):
    word_stack = [words[0]]
    # 비교를 편하게 하기 위해 첫문자는 넣어놓고 시작
    for idx, word in enumerate(words[1:]):
        check_word = word_stack[-1]
        # 같을 경우 제거
        if check_word == word:
            word_stack.pop()
        else:
            # 중복되지 않는 문자 넣는다.
            word_stack.append(word)
        # AAAA나 AA 같이 짝수개로 같은 문자가 있을 경우 하나가 추가된다.
        if not len(word_stack):
            word_stack.append(word)

    return ''.join(word_stack)


T = int(input())
for t in range(1, T+1):
    words = input()
    print('#{} {}'.format(t, remove(words)))
