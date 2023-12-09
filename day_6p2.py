if __name__ == '__main__':
    f = open('input_6.txt', 'r').readlines()
    time = int(f[0][:-1])
    distance = int(f[1])
    print(time, distance)
    first = 0
    last = 0

    for j in range(time):
        if j*(time-j) >= distance:
            first = j
            break

    print(first)

    for j in reversed(range(time)):
        if j*(time-j) >= distance:
            last = j
            break

    print(last)
    print(last - first + 1)
