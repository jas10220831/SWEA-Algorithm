checks = [1] * (10 ** 6 + 1)
checks[0] = 0
checks[1] = 0
for i in range(1, 10**6):
    if checks[i]:
        j = 2
        while i * j < 10**6:
            checks[i * j] = 0
            j += 1

for i in range(1, 10 ** 6):
    if checks[i]:
        print(i)
