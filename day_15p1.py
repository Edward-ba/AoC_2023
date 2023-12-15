if __name__ == '__main__':
    f = open('input_15.txt', 'r').read().split(',')

    out = []
    for i in f:
        tmp = 0
        for j in i:
            tmp += ord(j)
            tmp *= 17
            tmp %= 256
        out.append(tmp)
    print(sum(out))
