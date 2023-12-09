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
        if 5 in cards.values():
            value = 7
        elif 4 in cards.values():
            value = 6
        elif 3 in cards.values() and 2 in cards.values():
            value = 5
        elif 3 in cards.values() and 2 not in cards.values():
            value = 4
        elif list(cards.values()).count(2) == 2:
            value = 3
        elif list(cards.values()).count(2) == 1:
            value = 2
        elif list(cards.values()).count(1) == 5:
            value = 1
        hand = hand.replace('A', 'E')
        hand = hand.replace('T', 'A')
        hand = hand.replace('J', 'B')
        hand = hand.replace('Q', 'C')
        hand = hand.replace('K', 'D')
        sorter.append((str(value)+hand, bid))
    sorter.sort(key=lambda a: a[0])
    for i in range(len(sorter)):
        out += sorter[i][1]*(i+1)
    print(out)