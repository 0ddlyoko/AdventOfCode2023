import re

a = open("day6.txt").read().split("\n")


def resolve(lst):
    total = 1
    for z in lst:
        for i in range(0, z[0] // 2 + 1):
            y = i
            w = z[0] - i
            if y * w > z[1]:
                total *= z[0] - y * 2 + 1
                break
    return total


time = [int(z) for z in re.findall('[0-9]+', a[0][11:])]
distance = [int(z) for z in re.findall('[0-9]+', a[1][11:])]
b = [z for z in zip(time, distance)]
print("Part 1:", resolve([z for z in zip(time, distance)]))

time = [int("".join(re.findall('[0-9]+', a[0][11:])))]
distance = [int("".join(re.findall('[0-9]+', a[1][11:])))]
print("Part 2:", resolve([z for z in zip(time, distance)]))

print(time)
print(distance)
