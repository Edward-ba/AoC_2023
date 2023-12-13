import re


def replace_question_marks(string):
    output = []
    if '?' not in string:
        return [string]
    output += replace_question_marks(string.replace('?', '.', 1))
    output += replace_question_marks(string.replace('?', '#', 1))
    return output


if __name__ == '__main__':
    f = open('input_12.txt', 'r').readlines()
    f = [i[:-1] for i in f]
    out = 0
    for i in f:
        springs = i.partition(' ')[0]
        nums = i.partition(' ')[2].split(',')
        print(springs)
        print(nums)
        possibilities = replace_question_marks(springs)
        current_block = 0
        match_string = '\.*'
        for j in nums:
            match_string += '#' * int(j) + '\.{1,}'
        match_string = match_string[:-4] + '*'

        for j in possibilities:
            if re.fullmatch(match_string, j):
                out += 1
    print(out)
