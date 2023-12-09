
if __name__ == '__main__':
    out = 0
    f = open('input_2.txt', 'r').readlines()
    for i in f:
        min_r = 0
        min_g = 0
        min_b = 0
        rounds = i.partition(':')[2].strip(' ').strip('\n').split(';')
        for j in rounds:
            nums = j.strip(' ').split(', ')
            for k in nums:
                if 'red' in k and int(k.split(' ')[0]) > min_r:
                    min_r = int(k.split(' ')[0])
                if 'green' in k and int(k.split(' ')[0]) > min_g:
                    min_g = int(k.split(' ')[0])
                if 'blue' in k and int(k.split(' ')[0]) > min_b:
                    min_b = int(k.split(' ')[0])
        out += min_r * min_g * min_b
    print(out)
