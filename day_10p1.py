if __name__ == '__main__':
    f = open('input_10.txt', 'r').readlines()
    f = [[*i[:-1]] for i in f]
    cur_col = 0
    cur_row = 0
    for i in f:
        if 'S' in i:
            cur_col = i.index('S')
            cur_row = f.index(i)
    north_connectors = ['F', '|', '7']
    south_connectors = ['L', '|', 'J']
    west_connectors = ['F', '-', 'L']
    east_connectors = ['7', '-', 'J']

    path = [(cur_row, cur_col)]

    if f[cur_row][cur_col + 1] in east_connectors and (cur_row, cur_col + 1) not in path:
        cur_col += 1
    elif f[cur_row][cur_col - 1] in west_connectors and (cur_row, cur_col - 1) not in path:
        cur_col -= 1
    elif f[cur_row - 1][cur_col] in north_connectors and (cur_row - 1, cur_col) not in path:
        cur_row -= 1
    elif f[cur_row + 1][cur_col] in south_connectors and (cur_row + 1, cur_col) not in path:
        cur_row += 1

    path.append((cur_row, cur_col))

    while True:
        if len(path) != len(set(path)):
            break

        elif f[cur_row][cur_col] == '-':
            if f[cur_row][cur_col + 1] in east_connectors and (cur_row, cur_col + 1) not in path:
                cur_col += 1
            elif f[cur_row][cur_col - 1] in west_connectors and (cur_row, cur_col - 1) not in path:
                cur_col -= 1

        elif f[cur_row][cur_col] == '|':
            if f[cur_row - 1][cur_col] in north_connectors and (cur_row - 1, cur_col) not in path:
                cur_row -= 1
            elif f[cur_row + 1][cur_col] in south_connectors and (cur_row + 1, cur_col) not in path:
                cur_row += 1

        elif f[cur_row][cur_col] == 'J':
            if f[cur_row - 1][cur_col] in north_connectors and (cur_row - 1, cur_col) not in path:
                cur_row -= 1
            elif f[cur_row][cur_col - 1] in west_connectors and (cur_row, cur_col - 1) not in path:
                cur_col -= 1

        elif f[cur_row][cur_col] == '7':
            if f[cur_row][cur_col - 1] in west_connectors and (cur_row, cur_col - 1) not in path:
                cur_col -= 1
            elif f[cur_row + 1][cur_col] in south_connectors and (cur_row + 1, cur_col) not in path:
                cur_row += 1

        elif f[cur_row][cur_col] == 'L':
            if f[cur_row - 1][cur_col] in north_connectors and (cur_row - 1, cur_col) not in path:
                cur_row -= 1
            elif f[cur_row][cur_col + 1] in east_connectors and (cur_row, cur_col + 1) not in path:
                cur_col += 1

        elif f[cur_row][cur_col] == 'F':
            if f[cur_row][cur_col + 1] in east_connectors and (cur_row, cur_col + 1) not in path:
                cur_col += 1
            elif f[cur_row + 1][cur_col] in south_connectors and (cur_row + 1, cur_col) not in path:
                cur_row += 1

        path.append((cur_row, cur_col))
    print((len(path) - 1) / 2)