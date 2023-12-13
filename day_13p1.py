if __name__ == '__main__':
    f = open('input_13.txt', 'r').readlines()
    f = [i[:-1] for i in f]
    out = 0

    mirrors = []
    last = 0
    for i in range(len(f)):
        if f[i] == '':
            mirrors.append(f[last:i])
            last = i + 1

    for i in mirrors:
        broke = True
        for j in range(1, len(i)):
            if i[j] == i[j - 1]:
                works = False
                for k in range(j + 1):
                    if j - k - 1 < 0:
                        works = True
                        break
                    try:
                        if i[j - k - 1] != i[j + k]:
                            break
                    except IndexError:
                        works = True
                        break
                if works:
                    out += 100 * j
                    break
        else:
            broke = False

        if broke:
            continue

        vert = [[k[j] for k in i] for j in range(len(i[0]))]

        for j in range(1, len(vert)):
            if vert[j] == vert[j - 1]:
                works = False
                for k in range(j + 1):
                    if j - k - 1 < 0:
                        works = True
                        break
                    try:
                        if vert[j - k - 1] != vert[j + k]:
                            break
                    except IndexError:
                        works = True
                        break

                if works:
                    out += j
                    break
        else:
            print('no reflections?')
            break
    print(out)
