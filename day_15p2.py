if __name__ == '__main__':
    f = open('input_15.txt', 'r').read().split(',')

    hashmap = {j: [] for j in range(256)}
    for i in f:
        box_num = 0
        if '=' in i:
            label = i.partition('=')[0]
            box_num = 0
            for char in label:
                box_num += ord(char)
                box_num *= 17
                box_num %= 256
            for k in hashmap.keys():
                if label in [j[0] for j in hashmap[k]]:
                    if hashmap[k][[j[0] for j in hashmap[k]].index(label)][1] is None:
                        hashmap[k].pop([j[0] for j in hashmap[k]].index(label))
                        hashmap[k].append([label, i.partition('=')[2]])
                    else:
                        hashmap[k][[j[0] for j in hashmap[k]].index(label)] = [label, i.partition('=')[2]]
                    break
            else:
                hashmap[box_num].append([label, i.partition('=')[2]])
        elif '-' in i:
            label = i[:-1]
            for char in label:
                box_num += ord(char)
                box_num *= 17
                box_num %= 256
            for k in hashmap.keys():
                if label in [j[0] for j in hashmap[k]]:
                    hashmap[k][[j[0] for j in hashmap[k]].index(label)] = [label, None]
                    break
            else:
                hashmap[box_num].append([label, None])

    for i in list(hashmap.keys()):
        j = 0
        while j < len(hashmap[i]):
            if hashmap[i][j][1] is None:
                hashmap[i].remove([hashmap[i][j][0], hashmap[i][j][1]])
            else:
                j += 1

    print(hashmap)
    out = 0
    for i in hashmap.keys():
        for j in range(len(hashmap[i])):
            out += int(hashmap[i][j][1]) * (j + 1) * (i + 1)
    print(out)