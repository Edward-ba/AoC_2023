if __name__ == '__main__':
    f = open('input_11.txt', 'r').readlines()
    f = [[*i[:-1]] for i in f]

    no_galaxies_vert = []
    for i in range(len(f[0])):
        if '#' not in [j[i] for j in f]:
            no_galaxies_vert.append(i)
    for i in range(len(f)):
        for j in reversed(no_galaxies_vert):
            f[i].insert(j, '@')

    no_galaxies_horiz = []
    for i in range(len(f)):
        if '#' not in f[i]:
            no_galaxies_horiz.append(i)
    for i in reversed(no_galaxies_horiz):
        f.insert(i, ['@']*len(f[0]))

    galaxies = []
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == '#':
                galaxies.append((i, j))

    out = 0

    for i in galaxies:
        for j in galaxies[galaxies.index(i):]:
            if i[1] - j[1] < 0:
                for k in range(i[1], j[1]):
                    if f[i[0]][k] == '@':
                        out += 1000000 - 1
                    else:
                        out += 1
            else:
                for k in range(j[1], i[1]):
                    if f[i[0]][k] == '@':
                        out += 1000000 - 1
                    else:
                        out += 1
            if i[0] - j[0] < 0:
                for k in range(i[0], j[0]):
                    if f[k][i[1]] == '@':
                        out += 1000000 - 1
                    else:
                        out += 1
            else:
                for k in range(j[0], i[0]):
                    if f[k][i[1]] == '@':
                        out += 1000000 - 1
                    else:
                        out += 1
    print(out)
