import re

# this program could be a lot simpler, but I don't have the code from before, and I'm too lazy to rewrite it, so it's pretty much the same as p2
numbers = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}
if __name__ == '__main__':
    out = 0
    f = open('input_1.txt', 'r').readlines()
    for i in f:
        first = len(i) + 1
        first_num = 0
        for k in numbers.keys():
            if re.search(k, i) is not None and first > re.search(k, i).start():
                first = re.search(k, i).start()
                first_num = numbers[k]
        out += 10 * first_num
        last = -1
        last_num = 0
        for k in numbers.keys():
            if re.search('(?s:.*)'+k, i) is not None and last < re.search('(?s:.*)'+k, i).end():
                last = re.search('(?s:.*)'+k, i).end()
                last_num = numbers[k]
        out += last_num
    print(out)
