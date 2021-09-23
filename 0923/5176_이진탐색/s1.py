import sys
sys.stdin = open('sample_input.txt')


def inorder(idx):
    global now
    # check_numb 보다 큰 값은 나올 필요가 없다.
    if idx <= check_numb:
        inorder(idx * 2)
        tree[idx] = now
        now += 1
        inorder(idx * 2 + 1)


T = int(input())
for t in range(1, T+1):
    check_numb = int(input())
    # 입력할 숫자
    now = 1
    # 길이기 check_numb+1인 배열을 만들고 트리 같이 활용
    tree = [0] * (check_numb + 1)
    inorder(1)
    print('#{} {} {}'.format(t, tree[1], tree[check_numb//2]))