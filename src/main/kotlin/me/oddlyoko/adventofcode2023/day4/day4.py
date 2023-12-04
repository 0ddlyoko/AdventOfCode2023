a = [z.split(": ")[1][:-1] for z in open("day4.txt").readlines()]
b = [[[int(x) for x in y.split(" ") if x != ""] for y in z.split("|")] for z in a]
c = [len([y for y in z[1] if y in z[0]]) for z in b]
d = sum([int(2**(z - 1)) for z in c])
print("Part 1:", d)

numbers = [1] * len(c)
for z in enumerate(c, 1):
    idx = z[0]
    winner_number = z[1]
    for _ in range(numbers[idx - 1]):
        for x in range(winner_number):
            numbers[idx + x] += 1
print("Part 2:", sum(numbers))
