import re

if __name__ == '__main__':
    f = open('input_6.txt', 'r').readlines()
    times = f[0][:-1].split(' ')
    distances = f[1].split(' ')
    print(times, distances)
    out = 1
    for i in range(len(times)):
        works = 0
        for j in range(int(times[i])):
            if j*(int(times[i])-j) >= int(distances[i]):
                works += 1
        out *= works
    print(out)
