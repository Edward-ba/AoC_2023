import sys

f = open('input_16.txt', 'r').readlines()

f = [list(i[:-1]) for i in f]
sys.setrecursionlimit(100000000)


def follow(direction, start_row, start_col, energized):
    while True:
        if start_row >= len(f) or start_row < 0:
            break
        elif start_col >= len(f[start_row]) or start_col < 0:
            break
        elif (start_row, start_col, direction) in energized:
            break
        energized.append((start_row, start_col, direction))

        if f[start_row][start_col] == '.':
            if direction == 'up':
                start_row -= 1
            elif direction == 'down':
                start_row += 1
            elif direction == 'left':
                start_col -= 1
            elif direction == 'right':
                start_col += 1
        elif f[start_row][start_col] == '/':
            if direction == 'up':
                start_col += 1
                direction = 'right'
            elif direction == 'down':
                start_col -= 1
                direction = 'left'
            elif direction == 'left':
                start_row += 1
                direction = 'down'
            elif direction == 'right':
                start_row -= 1
                direction = 'up'
        elif f[start_row][start_col] == '\\':
            if direction == 'up':
                start_col -= 1
                direction = 'left'
            elif direction == 'down':
                start_col += 1
                direction = 'right'
            elif direction == 'left':
                start_row -= 1
                direction = 'up'
            elif direction == 'right':
                start_row += 1
                direction = 'down'
        elif f[start_row][start_col] == '-':
            if direction == 'up' or direction == 'down':
                energized = follow('right', start_row, start_col + 1, energized)
                energized = follow('left', start_row, start_col - 1, energized)
                break
            elif direction == 'left':
                start_col -= 1
            elif direction == 'right':
                start_col += 1
        elif f[start_row][start_col] == '|':
            if direction == 'left' or direction == 'right':
                energized = follow('down', start_row + 1, start_col, energized)
                energized = follow('up', start_row - 1, start_col, energized)
                break
            elif direction == 'down':
                start_row += 1
            elif direction == 'up':
                start_row -= 1

    return energized


if __name__ == '__main__':
    # brute force goes crazy
    max_energized = []
    for i in range(len(f)):
        print(i)
        tmp = follow('right', i, 0, [])
        tmp = [str(i[0]) + ' ' + str(i[1]) for i in tmp]
        tmp = list(dict.fromkeys(tmp))
        max_energized.append(len(tmp))

        tmp = follow('left', i, len(f[0]) - 1, [])
        tmp = [str(i[0]) + ' ' + str(i[1]) for i in tmp]
        tmp = list(dict.fromkeys(tmp))
        max_energized.append(len(tmp))
    for i in range(len(f[0])):
        print(i)
        tmp = follow('down', 0, i, [])
        tmp = [str(i[0]) + ' ' + str(i[1]) for i in tmp]
        tmp = list(dict.fromkeys(tmp))
        max_energized.append(len(tmp))

        tmp = follow('up', len(f) - 1, i, [])
        tmp = [str(i[0]) + ' ' + str(i[1]) for i in tmp]
        tmp = list(dict.fromkeys(tmp))
        max_energized.append(len(tmp))

    print(max(max_energized))