from math import gcd

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
    outs = []
    actual_i = 0
    cur_pos = [j for j in positions if j.endswith('A')]
    while len(cur_pos) > 0:
        if i >= len(path):
            i = 0
        if path[i] == 'L':
            cur_pos = [lefts[positions.index(j)] for j in cur_pos]
        elif path[i] == 'R':
            cur_pos = [rights[positions.index(j)] for j in cur_pos]
        i += 1
        actual_i += 1
        for j in cur_pos:
            if j.endswith('Z'):
                cur_pos.pop(cur_pos.index(j))
                outs.append(actual_i)

    ans = 1
    for x in outs:
        ans = (x * ans) // gcd(x, ans)
    print(ans)
