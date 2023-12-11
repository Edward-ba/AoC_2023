if __name__ == '__main__':
    f = open('input_11.txt', 'r').readlines()
    f = [[*i[:-1]] for i in f]
    no_galaxies_horiz = []
    for i in range(len(f)):
        if '#' not in f[i]:
            no_galaxies_horiz.append(i)
    for i in reversed(no_galaxies_horiz):
        f.insert(i, ['.']*len(f[0]))

    no_galaxies_vert = []
    for i in range(len(f[0])):
        if '#' not in [j[i] for j in f]:
            no_galaxies_vert.append(i)
    for i in range(len(f)):
        for j in reversed(no_galaxies_vert):
            f[i].insert(j, '.')

    galaxies = []
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == '#':
                galaxies.append((i, j))

    out = 0

    for i in galaxies:
        for j in galaxies[galaxies.index(i):]:
            out += abs(i[0] - j[0]) + abs(i[1] - j[1])

    print(out)
