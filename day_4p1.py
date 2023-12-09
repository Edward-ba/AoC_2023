if __name__ == '__main__':
    out = 0
    f = open('input_4.txt', 'r').readlines()
    for i in f:
        winning_numbers = i.partition(':')[2].partition('|')[0].split(' ')[1:-1]
        winning_numbers_worth = 0
        other_numbers = i.partition('|')[2].split(' ')[1:]
        other_numbers[-1] = other_numbers[-1][:-1]
        for j in other_numbers:
            if j == '':
                continue
            if j in winning_numbers:
                if winning_numbers_worth == 0:
                    winning_numbers_worth = 1
                else:
                    winning_numbers_worth *= 2
        out += winning_numbers_worth
    print(out)