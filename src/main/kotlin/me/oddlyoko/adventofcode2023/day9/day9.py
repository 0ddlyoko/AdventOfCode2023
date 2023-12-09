a = [[int(y) for y in z.split(" ")] for z in open("day9.txt").read().split("\n")]

all_z = []

for lst in a:
    z = [lst]
    current_lst_idx = 0
    found = False
    while not found:
        z += [[]]
        for i in range(len(z[current_lst_idx])):
            if i == 0:
                continue
            diff = z[current_lst_idx][i] - z[current_lst_idx][i - 1]
            z[current_lst_idx + 1] += [diff]

        if all(y == 0 for y in z[current_lst_idx + 1]):
            found = True
            break
        current_lst_idx += 1
    all_z += [z]


part_1 = 0
for z in all_z:
    # Now, sum the last digit of each list in z
    part_1 += sum([y[len(y) - 1] for y in z])
print("Part 1:", part_1)

part_2 = 0
for z in all_z:
    y = [y[0] for y in z]
    # Now, calculate the left digit
    result = 0
    for x in y[::-1]:
        b = x - result
        result = b
    part_2 += result
print("Part 2:", part_2)
