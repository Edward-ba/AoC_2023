if __name__ == '__main__':
    f = open('input_8.txt', 'r').readlines()
    path = f[0][:-1]
    positions = []
    lefts = []
    rights = []
    for i in f[2:]:
        positions.append(i[:-1][:3])
        lefts.append(i[:-1][7:10])
        rights.append(i[:-1][12:15])
    i = 0
    actual_i = 0
    cur_pos = 'AAA'
    while cur_pos != 'ZZZ':
        if i >= len(path):
            i = 0
        if path[i] == 'L':
            cur_pos = lefts[positions.index(cur_pos)]
            i += 1
            actual_i += 1
        elif path[i] == 'R':
            cur_pos = rights[positions.index(cur_pos)]
            i += 1
            actual_i += 1
    print(actual_i)