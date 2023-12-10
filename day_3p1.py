out = 0
f = open('input_3.txt', 'r').readlines()
for i in range(len(f)):
    j = 0
    while j < len(f[i][:-1]):
        number = ''
        if f[i][:-1][j].isnumeric():
            number += f[i][:-1][j]
            if f[i][:-1][j + 1].isnumeric():
                number += f[i][:-1][j + 1]
                if f[i][:-1][j + 2].isnumeric():
                    number += f[i][:-1][j + 2]
        else:
            j += 1
            continue
        print(number)

        if j - 1 < 0:
            pass
        elif f[i][:-1][j - 1] != '.':
            out += int(number)
            j += len(number)
            continue

        if j + len(number) >= len(f[i]) - 1:
            pass
        elif f[i][:-1][j + len(number)] != '.':
            out += int(number)
            j += len(number)
            continue

        for k in range(j - 1, j + len(number) + 1):
            if k < 0:
                continue
            if k >= len(f[i]) - 1:
                continue

            if i - 1 < 0:
                pass
            elif f[i - 1][:-1][k] != '.':
                out += int(number)
                break

            if i + 1 >= len(f):
                pass
            elif f[i + 1][:-1][k] != '.':
                out += int(number)
                break
        j += len(number)

print(out)
