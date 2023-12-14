map = [[y for y in z] for z in open("day14.txt").read().split("\n")]

ln = len(map)
nbr_of_cols = len(map[0])
nbr_of_rows = len(map)


def roll_north(the_map):
    new_map = [[y for y in z] for z in the_map]
    for col in range(nbr_of_cols):
        for row in range(nbr_of_rows):
            if new_map[row][col] == 'O':
                # Put it at the left whenever it's possible
                min_row = row
                for row_2 in range(row - 1, -1, -1):
                    if new_map[row_2][col] == '.':
                        min_row = row_2
                    else:
                        break
                new_map[row][col] = '.'
                new_map[min_row][col] = 'O'
    return new_map


def roll_west(the_map):
    new_map = [[y for y in z] for z in the_map]
    for row in range(nbr_of_rows):
        for col in range(nbr_of_cols):
            if new_map[row][col] == 'O':
                # Put it at the left whenever it's possible
                min_col = col
                for col_2 in range(col - 1, -1, -1):
                    if new_map[row][col_2] == '.':
                        min_col = col_2
                    else:
                        break
                new_map[row][col] = '.'
                new_map[row][min_col] = 'O'
    return new_map


def roll_south(the_map):
    new_map = [[y for y in z] for z in the_map]
    for col in range(nbr_of_cols):
        for row in range(nbr_of_rows - 1, -1, -1):
            if new_map[row][col] == 'O':
                # Put it at the right whenever it's possible
                max_row = row
                for row_2 in range(row + 1, nbr_of_rows):
                    if new_map[row_2][col] == '.':
                        max_row = row_2
                    else:
                        break
                new_map[row][col] = '.'
                new_map[max_row][col] = 'O'
    return new_map


def roll_east(the_map):
    new_map = [[y for y in z] for z in the_map]
    for row in range(nbr_of_rows):
        for col in range(nbr_of_cols - 1, -1, -1):
            if new_map[row][col] == 'O':
                # Put it at the right whenever it's possible
                min_col = col
                for col_2 in range(col + 1, nbr_of_cols):
                    if new_map[row][col_2] == '.':
                        min_col = col_2
                    else:
                        break
                new_map[row][col] = '.'
                new_map[row][min_col] = 'O'
    return new_map


def calculate(the_map):
    result = 0
    for i in range(len(the_map)):
        count = len([1 for z in the_map[i] if z == 'O'])
        result += (len(the_map) - i) * count

    return result


def print_map(the_map):
    for a in the_map:
        print(a)


part_1_new_map = roll_north(map)
part_1 = calculate(part_1_new_map)
print("Part 1:", part_1)


storage = {}
a = False
b = None


def do_the_roll(i, the_map):
    global a, b

    key = str(the_map)
    if key in storage:
        if not a:
            b = the_map
            a = True
        if b == the_map:
            pass

        print(i)
        return storage[key]
    result = roll_north(the_map)
    result = roll_west(result)
    result = roll_south(result)
    result = roll_east(result)
    storage[key] = result
    return result


part_2 = 0

the_map = map
# We saw after testing that after 10 iteration, the result repeats every 7 iteration:
# 10, 17, 24, 31, ...
# This is for the testing data. Now, for the real data, after 181 iterations, the result repeats every 18 iteration:
# 181, 199, 217, 235, ...
# We hardcode this value here, as I have la flemme to fix it programmatically
for i in range(181):
    the_map = do_the_roll(i, the_map)
map_after_10 = the_map
a = 1_000_000_000 - 181
iteration_to_add = a - ((a // 18) * 18)
for i in range(iteration_to_add):
    the_map = do_the_roll(i, the_map)


print_map(the_map)
part_2 = calculate(the_map)
print("Part 2:", part_2)

