map = [z for z in open("day11.txt").read().split("\n")]

# Rows
rows = []
for i, z in enumerate(map):
    if '#' not in z:
        rows.append(i)

# Cols
cols = []
for i in range(len(map[0])):
    if not any(z[i] == '#' for z in map):
        cols.append(i)

# Galaxies
galaxies = []
for i, z in enumerate(map):
    for j, y in enumerate(map[i]):
        if y == '#':
            galaxies.append((i, j))

# Now that we have galaxies, calculate all possible combination


def get_number_of_passed_values(min_x, max_x, vals):
    """
    Calculate the amount of times we have an element in vals that is between min_x & max_x
    """
    result = 0
    for val in vals:
        if min_x < val < max_x:
            result += 1
    return result


def calculate(distance):
    result = 0
    for x, galaxy in enumerate(galaxies):
        for y, galaxy_2 in enumerate(galaxies[x:]):
            if galaxy == galaxy_2:
                continue
            min_x = min(galaxy[0], galaxy_2[0])
            max_x = max(galaxy[0], galaxy_2[0])
            min_y = min(galaxy[1], galaxy_2[1])
            max_y = max(galaxy[1], galaxy_2[1])

            number_of_empty_x = get_number_of_passed_values(min_x, max_x, rows) * distance
            number_of_empty_y = get_number_of_passed_values(min_y, max_y, cols) * distance

            diff_x = max_x - min_x + number_of_empty_x
            diff_y = max_y - min_y + number_of_empty_y
            result += diff_x + diff_y
    return result


part_1 = calculate(1)
print("Part 1:", part_1)


# Idk why I need to remove 1, but it works :D
part_2 = calculate(1000000 - 1)
print("Part 2:", part_2)
