import sys
f = open('input_16.txt', 'r').readlines()

f = [list(i[:-1]) for i in f]
energized = []
sys.setrecursionlimit(100000)


def follow(direction, start_row, start_col):
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
                follow('right', start_row, start_col + 1)
                follow('left', start_row, start_col - 1)
                break
            elif direction == 'left':
                start_col -= 1
            elif direction == 'right':
                start_col += 1
        elif f[start_row][start_col] == '|':
            if direction == 'left' or direction == 'right':
                follow('down', start_row + 1, start_col)
                follow('up', start_row - 1, start_col)
                break
            elif direction == 'down':
                start_row += 1
            elif direction == 'up':
                start_row -= 1


if __name__ == '__main__':
    follow('right', 0, 0)
    print(energized)
    energized = [str(i[0]) + ' ' + str(i[1]) for i in energized]

    energized = list(dict.fromkeys(energized))

    print(len(energized))