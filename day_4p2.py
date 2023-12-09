def get_card_wins(card):
    winning_numbers = card.partition(':')[2].partition('|')[0].split(' ')[1:-1]
    matches = 0
    other_numbers = card.partition('|')[2].split(' ')[1:]
    other_numbers[-1] = other_numbers[-1][:-1]
    for k in other_numbers:
        if k == '':
            continue
        if k in winning_numbers:
            matches += 1
    return matches


if __name__ == '__main__':
    f = open('input_4.txt', 'r').readlines()
    number_of_cards = [1] * len(f)
    for i in range(len(f)):
        wins = get_card_wins(f[i])
        for j in range(i+1, i+wins+1):
            number_of_cards[j] += number_of_cards[i]
    print(sum(number_of_cards))
