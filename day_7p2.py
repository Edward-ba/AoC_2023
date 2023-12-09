if __name__ == '__main__':
    f = open('input_7.txt', 'r').readlines()
    sorter = []
    out = 0
    for i in range(len(f)):
        hand, bid = f[i][:-1].split(' ')
        bid = int(bid)
        cards = {
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            'T': 0,
            'J': 0,
            'Q': 0,
            'K': 0,
            'A': 0,
        }
        for j in hand:
            cards[j] += 1
        cards_not_joker = [value for key, value in cards.items() if key != 'J']

        if 5 in cards.values() or (4 in cards_not_joker and cards['J'] == 1) or (3 in cards_not_joker and cards['J'] == 2) or (2 in cards_not_joker and cards['J'] == 3) or (1 in cards_not_joker and cards['J'] == 4):
            value = 7
        elif 4 in cards.values() or (3 in cards_not_joker and cards['J'] == 1) or (2 in cards_not_joker and cards['J'] == 2) or (1 in cards_not_joker and cards['J'] == 3):
            value = 6
        elif (3 in cards.values() and 2 in cards.values()) or (cards_not_joker.count(2) == 2 and cards['J'] == 1) or ((3 in cards_not_joker) and cards['J'] == 2):
            value = 5
        elif 3 in cards.values() or (2 in cards_not_joker and cards['J'] == 1) or (1 in cards_not_joker and cards['J'] == 2):
            value = 4
        elif list(cards.values()).count(2) == 2:
            value = 3
        elif list(cards.values()).count(2) == 1 or cards['J'] == 1:
            value = 2
        elif list(cards.values()).count(1) == 5:
            value = 1
        hand = hand.replace('A', 'E')
        hand = hand.replace('T', 'A')
        hand = hand.replace('J', '1')
        hand = hand.replace('Q', 'C')
        hand = hand.replace('K', 'D')
        sorter.append((str(value)+hand, bid))
    sorter.sort(key=lambda a: a[0])
    for i in range(len(sorter)):
        out += sorter[i][1]*(i+1)
    print(out)