a = [[z.split(" ")[0], int(z.split(" ")[1])] for z in open("day7.txt").read().split("\n")]
LST = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
LST_JOKER = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
J_POS = LST_JOKER.index('J')


def sort_by_strength(lst, is_joker=False):
    # First, check if we have a pair, two pair, a three of a kind, ...
    result = []
    for hand, bid in lst:
        strong = 0
        number_of_occurrence = [0] * len(LST)
        hand_strong = []
        for idx, card in enumerate(hand):
            card_idx = LST_JOKER.index(card) if is_joker else LST.index(card)
            number_of_occurrence[card_idx] += 1
            hand_strong.append(card_idx)
        if 5 in number_of_occurrence:
            strong = 7
        elif 4 in number_of_occurrence:
            if is_joker and number_of_occurrence[J_POS]:
                strong = 7
            else:
                strong = 6
        elif 3 in number_of_occurrence and 2 in number_of_occurrence:
            if is_joker and number_of_occurrence[J_POS]:
                strong = 7
            else:
                strong = 5
        elif 3 in number_of_occurrence:
            if is_joker and number_of_occurrence[J_POS]:
                strong = 6
            else:
                strong = 4
        elif 2 in number_of_occurrence:
            if len([z for z in number_of_occurrence if z == 2]) == 2:
                if is_joker and number_of_occurrence[J_POS]:
                    if number_of_occurrence[J_POS] == 1:
                        strong = 5
                    else:
                        strong = 6
                else:
                    strong = 3
            else:
                if is_joker and number_of_occurrence[J_POS]:
                    strong = 4
                else:
                    strong = 2
        else:
            if is_joker and number_of_occurrence[J_POS]:
                strong = 2
            else:
                strong = 1
        result.append([hand, bid, strong, hand_strong])
    result.sort(key=lambda h: (h[2], h[3]))
    return result


part_1 = 0
b = sort_by_strength(a)
print(b)
for idx, card in enumerate(b, 1):
    part_1 += idx * card[1]

print("Part 1:", part_1)


part_2 = 0
b = sort_by_strength(a, is_joker=True)
print(b)
for idx, card in enumerate(b, 1):
    z = idx * card[1]
    part_2 += z

print("Part 2:", part_2)
print(b)
