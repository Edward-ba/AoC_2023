if __name__ == '__main__':
    f = open('input_14.txt', 'r').readlines()
    f = [list(i[:-1]) for i in f]
    tmp = 0
    lastseen = {}
    skipped = False
    N = 1000000000
    while tmp < N:
        for i in range(len(f)):
            for j in range(len(f[0])):
                if f[i][j] == 'O':
                    for k in range(1, i + 1):
                        if i - k < 0:
                            break
                        if f[i - k][j] == '.':
                            f[i - k][j] = 'O'
                            f[i - k + 1][j] = '.'
                        else:
                            break

        for i in range(len(f)):
            for j in range(len(f[0])):
                if f[i][j] == 'O':
                    for k in range(1, j + 1):
                        if j - k < 0:
                            break
                        if f[i][j - k] == '.':
                            f[i][j - k] = 'O'
                            f[i][j - k + 1] = '.'
                        else:
                            break

        for i in range(len(f)):
            for j in range(len(f[0])):
                if f[len(f) - i - 1][j] == 'O':
                    for k in range(1, len(f)):
                        if len(f) - i - 1 + k >= len(f):
                            break
                        if f[len(f) - i - 1 + k][j] == '.':
                            f[len(f) - i - 1 + k][j] = 'O'
                            f[len(f) - i - 1 + k - 1][j] = '.'
                        else:
                            break

        for i in range(len(f)):
            for j in range(len(f[0])):
                if f[i][len(f[0]) - j - 1] == 'O':
                    for k in range(1, len(f[0])):
                        if len(f[0]) - j - 1 + k >= len(f[0]):
                            break
                        if f[i][len(f[0]) - j - 1 + k] == '.':
                            f[i][len(f[0]) - j - 1 + k] = 'O'
                            f[i][len(f[0]) - j - 1 + k - 1] = '.'
                        else:
                            break

        sig = hash(tuple(tuple(i) for i in f))
        if not skipped and sig in lastseen:
            cycle = tmp - lastseen[sig]
            skips = 1 + cycle * ((N - tmp) // cycle)
            tmp += skips

            skipped = True
        else:
            lastseen[sig] = tmp
            tmp += 1

    out = 0
    for i in range(len(f)):
        for j in f[i]:
            if j == 'O':
                out += (len(f) - i)
    print(out)
