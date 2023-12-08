for i in range(15):
    for j in range(15 - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()


for i in range(15):
    for j in range(i + 1):
        print(' ', end='')
    for k in range(2 * (14 - i) - 1):
        print('*', end='')
    print()
