
if __name__ == '__main__':
    out = 0
    f = open('input_2.txt', 'r').readlines()
    for i in f:
        works = True
        rounds = i.partition(':')[2].strip(' ').strip('\n').split(';')
        for j in rounds:
            nums = j.strip(' ').split(', ')
            for k in nums:
                if 'red' in k and int(k.split(' ')[0]):
                    works = False
                    break
                if 'green' in k and int(k.split(' ')[0]) > 13:
                    works = False
                    break
                if 'blue' in k and int(k.split(' ')[0]) > 14:
                    works = False
                    break
        if works:
            out += int(i.partition(':')[0][5:])  # game number
    print(out)
