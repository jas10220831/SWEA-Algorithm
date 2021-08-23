def no_vowel(word):
    # 모음인지 확인하기 위한 리스트를 만든다.
    vowel = ['a', 'e', 'i', 'o', 'u']
    # 새로운 단어를 입력할 변수를 만든다.
    new_word = ''
    # 탐색하며 모음이 아니면 new_word에 추가한다.
    for alpha in word:
        if not alpha in vowel:
            new_word += alpha
    return new_word


T = int(input())
for t in range(1, T+1):
    word = str(input())
    print('#{} {}'.format(t, no_vowel(word)))

