

if __name__ == '__main__':
    f = open('input_5.txt', 'r').readlines()
    seeds = f[0].partition(': ')[2][:-1].split(' ')

    seed_to_soil_map = []
    stf = []
    ftw = []
    wtl = []
    ltt = []
    tth = []
    htl = []

    for i in f[f.index('seed-to-soil map:\n')+1:f.index('soil-to-fertilizer map:\n')-1]:
        seed_to_soil_map.append(i[:-1].split(' '))
    for i in f[f.index('soil-to-fertilizer map:\n')+1:f.index('fertilizer-to-water map:\n')-1]:
        stf.append(i[:-1].split(' '))
    for i in f[f.index('fertilizer-to-water map:\n')+1:f.index('water-to-light map:\n')-1]:
        ftw.append(i[:-1].split(' '))
    for i in f[f.index('water-to-light map:\n')+1:f.index('light-to-temperature map:\n')-1]:
        wtl.append(i[:-1].split(' '))
    for i in f[f.index('light-to-temperature map:\n')+1:f.index('temperature-to-humidity map:\n')-1]:
        ltt.append(i[:-1].split(' '))
    for i in f[f.index('temperature-to-humidity map:\n') + 1:f.index('humidity-to-location map:\n') - 1]:
        tth.append(i[:-1].split(' '))
    for i in f[f.index('humidity-to-location map:\n')+1:]:
        htl.append(i[:-1].split(' '))

    location = []
    for i in seeds:
        found = False
        for j in seed_to_soil_map:
            if int(j[1]) <= int(i) < int(j[1])+int(j[2]):
                tmp = int(j[0])+(int(i)-int(j[1]))
                found = True
                break
        if not found:
            tmp = int(i)

        for j in stf:
            if int(j[1]) <= tmp < int(j[1])+int(j[2]):
                tmp = int(j[0])+(tmp-int(j[1]))
                break

        for j in ftw:
            if int(j[1]) <= tmp < int(j[1])+int(j[2]):
                tmp = int(j[0])+(tmp-int(j[1]))
                break

        for j in wtl:
            if int(j[1]) <= tmp < int(j[1])+int(j[2]):
                tmp = int(j[0])+(tmp-int(j[1]))
                break

        for j in ltt:
            if int(j[1]) <= tmp < int(j[1])+int(j[2]):
                tmp = int(j[0])+(tmp-int(j[1]))
                break

        for j in tth:
            if int(j[1]) <= tmp < int(j[1])+int(j[2]):
                tmp = int(j[0])+(tmp-int(j[1]))
                break

        found = False
        for j in htl:
            if int(j[1]) <= tmp < int(j[1])+int(j[2]):
                location.append(int(j[0])+(tmp-int(j[1])))
                found = True
                break
        if not found:
            location.append(tmp)
    print(location)
    print(min(location))
