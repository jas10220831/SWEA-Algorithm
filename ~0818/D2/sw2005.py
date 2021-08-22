

T = int(input())

for t in range(1,T+1):
    print(f'#{t}')

    N = int(input())
    list1 = [1]
    list2 = [1]
    #n번쨰 값을 계산
    if N == 1:
        print(1)
    else:
        print(1)
        for n in range(2,N+1):
            #N = 1 일 경우 1만 출력
            for j in range(1,n-1):
                #list2[j] = list1[j-1]+list1[j\]
                list2.append(list1[j-1]+list1[j])
            list2.append(1)
            for number in list2:
                print(number, end = ' ')
            print()
            list1 = list2[:]
            list2 = [1]