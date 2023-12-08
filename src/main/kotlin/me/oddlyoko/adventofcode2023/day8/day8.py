import math

a = open("day8.txt").read().split("\n")
instructions = a[0]

paths = a[2:]
paths = {z.split(" = ")[0]: z.split(" = ")[1][1:-1].split(", ") for z in paths}

part_1 = 0
current_path = "AAA"
while True:
    for instruction in instructions:
        part_1 += 1
        if instruction == 'R':
            current_path = paths[current_path][1]
        else:
            current_path = paths[current_path][0]
    if current_path == "ZZZ":
        break

print("Part 1:", part_1)

part_2 = 0
current_paths = [path for path in paths if path[2] == 'A']
all_path_idx = []
all_path_diff = []
for i in range(len(current_paths)):
    all_path_idx.append([])
    all_path_diff.append([])
done = False
# First, we will go along a lot of path in order to find a common path for each
while True:
    for instruction in instructions:
        part_2 += 1
        for idx, current_path in enumerate(current_paths):
            if current_path[2] == 'Z':
                all_path_idx[idx].append(part_2)
                z = len(all_path_idx[idx]) - 2
                all_path_diff[idx].append(part_2 - all_path_idx[idx][z if z >= 0 else 0])
            if instruction == 'R':
                current_paths[idx] = paths[current_path][1]
            else:
                current_paths[idx] = paths[current_path][0]
        if part_2 % 100000 == 0:
            done = True
            break
        if all([current_path[2] == 'Z' for current_path in current_paths]):
            done = True
            break
    if done:
        break


# Update: After testing, I saw that the "diff" is exactly the same for each Ghost (21883 for first ghost, 19667 for second, ...)
# So, we only need to find the ppcm (lcm) of all "diff"
numbers = [path[1] for path in all_path_diff]

part_2 = math.lcm(*numbers)

print("Part 2:", part_2)


