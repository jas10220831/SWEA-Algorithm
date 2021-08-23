import sys
sys.stdin = open('input.txt')


def encoding(words, encoding_len, encodings):
    # I x y s : x 다음부터 y개의 숫자 s들을 추가한다.
    # D x y : x 다음부터 y개의 숫자르 ㄹ지운다.
    # A y s : y개의 숫자 s들을 맨뒤에 추가한다.

    # 명령어의 위치를 표시할 변수
    idx = 0
    # 명령어 횟수 만큼 반복한다.
    for _ in range(encoding_len):
        a = encodings[idx]
        # A 일 경우
        if encodings[idx] == 'A':
            # 앞으로 한칸 이동
            idx += 1
            # y 개의 숫자 s 들을 append
            for _ in range(encodings[idx]):
                # 앞으로 한칸 또 이동
                idx += 1
                words.append(encodings[idx])

        # I 일 경우
        if encodings[idx] == 'I':
            # 앞으로 이동
            idx += 1
            # 새로운 숫자들을 입력할 자리 표시
            insert_idx = encodings[idx]
            # 앞으로 이동하여 명령어 입력
            idx += 1
            for _ in range(encodings[idx]):
                idx += 1
                words.insert(insert_idx, encodings[idx])
                # 다음 자리에 숫자를 추가해야 한다.
                insert_idx += 1

        if encodings[idx] == 'D':
            # D 일 경우
            idx += 1
            # 삭제할 숫자들의 idx
            delete_idx = encodings[idx]
            idx += 1
            # 숫자 개수
            delete_count = encodings[idx]
            # 숫자 개수만큼 삭제
            for _ in range(delete_count):
                words.pop(delete_idx)
        idx += 1



    return words[:10]


# encodings를 받을 때 숫자 문자 구분
def change(word):
    try:
        int(word)
        return int(word)
    except:
        return word


for t in range(1, 11):
    numbers_len = int(input())
    numbers = list(map(int, input().split()))
    encodings_len = int(input())
    encodings = list(map(change, input().split()))
    print('#{}'.format(t), end = ' ')
    print(*encoding(numbers, encodings_len, encodings))