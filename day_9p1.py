if __name__ == '__main__':
    f = open('input_9.txt', 'r').readlines()
    lst = [j[:-1].split(' ') for j in f]
    out = 0
    for i in lst:
        diffs = [[int(j) for j in i]]
        while not all([k == 0 for k in diffs[len(diffs) - 1]]):
            tmp = []
            for j in range(len(diffs[len(diffs) - 1]) - 1):
                tmp.append(diffs[len(diffs) - 1][j+1] - diffs[len(diffs) - 1][j])
            diffs.append(tmp)
        for j in diffs:
            out += j[len(j) - 1]
    print(out)
