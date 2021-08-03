N = int(input())


for number in range(1, N+1):
    clap = 0
    answer = str(number)
    for idx in ['3','6','9']:
        clap += answer.count(idx)
    if clap == 0 :
        answer = str(number)
    else :
        answer = '-' * clap

    print(answer, end = ' ')

