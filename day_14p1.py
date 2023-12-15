if __name__ == '__main__':
    f = open('input_14.txt', 'r').readlines()
    f = [list(i[:-1]) for i in f]
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == 'O':
                for k in range(1, i + 1):
                    if i - k < 0:
                        break
                    if f[i - k][j] == '.':
                        f[i - k][j] = 'O'
                        f[i - k + 1][j] = '.'
                    else:
                        break

    out = 0
    for i in range(len(f)):
        for j in f[i]:
            if j == 'O':
                out += (len(f) - i)
    print(out)