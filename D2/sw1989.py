T = int(input())

for t in range(1,T+1):
    word = input()
    new_word = ''
    for i in range(-1,-len(word)-1,-1):
        new_word += word[i]
    if word == new_word:
        print(f'#{t} 1')
    else :
        print(f'#{t} 0')
