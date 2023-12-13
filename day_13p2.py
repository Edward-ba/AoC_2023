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
        smudge_fixed = False
        for j in range(1, len(i)):
            first_match = False
            for h in range(len(i[j - 1])):
                tmp = i[j]
                if tmp[h] == '.':
                    tmp = list(tmp)
                    tmp[h] = '#'
                    tmp = ''.join(tmp)
                else:
                    tmp = list(tmp)
                    tmp[h] = '.'
                    tmp = ''.join(tmp)
                if tmp == i[j - 1]:
                    smudge_fixed = True
                    first_match = True
                    break
            if i[j] == i[j - 1] or first_match:
                works = False
                for k in range(1, j + 1):
                    if j - k - 1 < 0:
                        works = True
                        break
                    try:
                        if i[j - k - 1] != i[j + k]:
                            if smudge_fixed:
                                smudge_fixed = False
                                break
                            else:
                                for h in range(len(i[0])):
                                    tmp = i[j - k - 1]
                                    if tmp[h] == '.':
                                        tmp = list(tmp)
                                        tmp[h] = '#'
                                        tmp = ''.join(tmp)
                                    else:
                                        tmp = list(tmp)
                                        tmp[h] = '.'
                                        tmp = ''.join(tmp)
                                    if tmp == i[j + k]:
                                        smudge_fixed = True
                                        break
                                else:
                                    break
                    except IndexError:
                        works = True
                        break
                if works and smudge_fixed:
                    out += 100 * j
                    break
        else:
            broke = False

        if broke:
            continue

        vert = [[k[j] for k in i] for j in range(len(i[0]))]
        smudge_fixed = False
        for j in range(1, len(vert)):
            first_match = False
            for h in range(len(vert[j - 1])):
                tmp = vert[j].copy()
                if tmp[h] == '.':
                    tmp[h] = '#'
                else:
                    tmp[h] = '.'
                if tmp == vert[j - 1]:
                    smudge_fixed = True
                    first_match = True
                    break
            if vert[j] == vert[j - 1] or first_match:
                works = False
                for k in range(1, j + 1):
                    if j - k - 1 < 0:
                        works = True
                        break
                    try:
                        if vert[j - k - 1] != vert[j + k]:
                            if smudge_fixed:
                                smudge_fixed = False
                                break
                            else:
                                for h in range(len(vert[0])):
                                    tmp = vert[j - k - 1].copy()
                                    if tmp[h] == '.':
                                        tmp[h] = '#'
                                    else:
                                        tmp[h] = '.'
                                    if tmp == vert[j + k]:
                                        smudge_fixed = True
                                        break
                                else:
                                    break
                    except IndexError:
                        works = True
                        break
                if works and smudge_fixed:
                    out += j
                    break
        else:
            print('no reflections?')
            break
    print(out)
