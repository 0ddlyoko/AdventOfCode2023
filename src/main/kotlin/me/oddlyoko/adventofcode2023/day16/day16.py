import queue
map = [z for z in open("day16.txt").read().split("\n")]
number_of_cols = len(map[0])
number_of_rows = len(map)


def resolve(start_queue):
    final_map = [['.' for _ in range(number_of_cols)] for _ in range(number_of_rows)]
    already_done = set()
    # Queue containing [(x, y), (x_dir, y_dir)]
    q1 = queue.Queue()
    q1.put(start_queue)
    while not q1.empty():
        ([x, y], [x_dir, y_dir]) = q1.get()
        if x < 0 or x >= number_of_cols or y < 0 or y >= number_of_rows:
            continue
        current_slot = map[y][x]
        key = f"{x}-{y}-{x_dir}-{y_dir}"
        if key in already_done:
            continue
        final_map[y][x] = '#'
        already_done.add(key)
        if current_slot == '.':
            # Continue
            q1.put([(x + x_dir, y + y_dir), (x_dir, y_dir)])
        elif current_slot == '|':
            if x_dir != 0:
                q1.put([(x, y - 1), (0, -1)])
                q1.put([(x, y + 1), (0, 1)])
            else:
                q1.put([(x + x_dir, y + y_dir), (x_dir, y_dir)])
        elif current_slot == '-':
            if x_dir != 0:
                q1.put([(x + x_dir, y + y_dir), (x_dir, y_dir)])
            else:
                q1.put([(x - 1, y), (-1, 0)])
                q1.put([(x + 1, y), (1, 0)])
        elif current_slot == '/':
            if x_dir != 0:
                q1.put([(x, y - x_dir), (0, -x_dir)])
            else:
                q1.put([(x - y_dir, y), (-y_dir, 0)])
        elif current_slot == '\\':
            if x_dir != 0:
                q1.put([(x, y + x_dir), (0, x_dir)])
            else:
                q1.put([(x + y_dir, y), (y_dir, 0)])
    return final_map


def print_map(the_map):
    for a in the_map:
        print(a)


def count_tiles(the_map):
    result = 0
    for line in the_map:
        for row in line:
            if row == '#':
                result += 1
    return result


part_1 = count_tiles(resolve([(0, 0), (1, 0)]))
print("Part 1:", part_1)


part_2 = 0
# Top, Bot
for i in range(number_of_cols):
    count = count_tiles(resolve([(i, 0), (0, 1)]))
    if count > part_2:
        part_2 = count
    count = count_tiles(resolve([(i, number_of_rows - 1), (0, -1)]))
    if count > part_2:
        part_2 = count

# Left, Right
for i in range(number_of_rows):
    count = count_tiles(resolve([(0, i), (1, 0)]))
    if count > part_2:
        part_2 = count
    count = count_tiles(resolve([(number_of_cols - 1, i), (-1, 0)]))
    if count > part_2:
        part_2 = count


print("Part 2:", part_2)












