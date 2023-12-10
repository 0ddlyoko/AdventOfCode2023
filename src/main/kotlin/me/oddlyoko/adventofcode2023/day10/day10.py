import queue

map = [z for z in open("day10.txt").read().split("\n")]

s_pos = [0, 0]
for z in range(len(map)):
    if 'S' in map[z]:
        s_pos = [z, map[z].index('S')]
        break

current_pos = [s_pos[0], s_pos[1]]
direction = [0, 0]
# Check where we start.
# We assume s_pos is not in a corner
if map[current_pos[0]][current_pos[1] + 1] in ['-', 'J', '7']:
    current_pos[1] += 1
    direction = [0, 1]
elif map[current_pos[0]][current_pos[1] - 1] in ['-', 'F', 'L']:
    current_pos[1] -= 1
    direction = [0, -1]
elif map[current_pos[0] + 1][current_pos[1]] in ['|', 'J', 'L']:
    current_pos[0] += 1
    direction = [1, 0]
elif map[current_pos[0] - 1][current_pos[1]] in ['|', 'F', '7']:
    current_pos[0] -= 1
    direction = [-1, 0]

part_1 = 0
tiles_for_part_2 = [['.'] * len(z) for z in map]
while True:
    part_1 += 1
    current_pipe = map[current_pos[0]][current_pos[1]]
    tiles_for_part_2[current_pos[0]][current_pos[1]] = current_pipe
    if current_pipe == '-':
        # Direction doesn't change
        pass
    elif current_pipe == '|':
        # Direction doesn't change
        pass
    elif current_pipe == 'J':
        if direction[0]:
            # North => West
            direction = [0, -1]
        else:
            # West => North
            direction = [-1, 0]
    elif current_pipe == 'L':
        if direction[0]:
            # North => East
            direction = [0, 1]
        else:
            # East => North
            direction = [-1, 0]
    elif current_pipe == 'F':
        if direction[0]:
            # South => East
            direction = [0, 1]
        else:
            # East => South
            direction = [1, 0]
    elif current_pipe == '7':
        if direction[0]:
            # South => West
            direction = [0, -1]
        else:
            # West => South
            direction = [1, 0]
    elif current_pipe == 'S':
        break
    current_pos[0] += direction[0]
    current_pos[1] += direction[1]


print("Part 1:", part_1 // 2)
# print("Real tiles:", tiles_for_part_2)

# Here is a solution to part 2:
# First, we scale up the labyrinth by adding points between tiles
# Second, we fill those tiles with the walls of the labyrinth
# Third, we start from the first point, and we fill it and all his neighbour by an 'O'
# Then, Complete it for each border with an '.'
# Finally, all points that are not filled are the ones where there is not a direct link to an edge


# def print_map(the_map):
#     for a in the_map:
#         print(a)


# First, we scale up the labyrinth by adding points between tiles
# print_map(tiles_for_part_2)
# print("\n")
new_map_width = len(tiles_for_part_2[0]) * 2 + 1
new_map_height = len(tiles_for_part_2) * 2 + 1
scaled_map = [['.'] * new_map_width]
for m in tiles_for_part_2:
    scaled_map.append(list('.' + '.'.join(m) + '.'))
    # Add line between it filled with dots
    scaled_map.append(['.'] * new_map_width)

# print("Scaled Map:")
# print_map(scaled_map)
# print("End Scaled Map")

# Second, we fill those tiles with the walls of the labyrinth
for x in range(len(tiles_for_part_2)):
    line = tiles_for_part_2[x]
    for y in range(len(line)):
        current_x = x * 2 + 1
        current_y = y * 2 + 1
        current_pipe = scaled_map[current_x][current_y]
        if current_pipe == '|':
            scaled_map[current_x - 1][current_y] = '|'
            scaled_map[current_x + 1][current_y] = '|'
        elif current_pipe == '-':
            scaled_map[current_x][current_y - 1] = '-'
            scaled_map[current_x][current_y + 1] = '-'
        elif current_pipe == 'L':
            scaled_map[current_x - 1][current_y] = '|'
            scaled_map[current_x][current_y + 1] = '-'
        elif current_pipe == 'J':
            scaled_map[current_x - 1][current_y] = '|'
            scaled_map[current_x][current_y - 1] = '-'
        elif current_pipe == '7':
            scaled_map[current_x][current_y - 1] = '-'
            scaled_map[current_x + 1][current_y] = '|'
        elif current_pipe == 'F':
            scaled_map[current_x][current_y + 1] = '-'
            scaled_map[current_x + 1][current_y] = '|'

# Third, we start from the first point, and we fill it and all his neighbour by an 'O'
# Then, continue for each border with an '.'
points_to_check = queue.Queue()

# Top & Bot
for x in range(new_map_width):
    # Top
    if scaled_map[0][x] == '.':
        points_to_check.put((0, x))
    # Bot
    if scaled_map[new_map_height - 1][x] == '.':
        points_to_check.put((new_map_height - 1, x))

# Left & Right
for x in range(new_map_height):
    # Left
    if scaled_map[x][0] == '.':
        points_to_check.put((x, 0))
    # Right
    if scaled_map[x][new_map_width - 1] == '.':
        points_to_check.put((x, new_map_width - 1))

# Fill it
while not points_to_check.empty():
    pos = points_to_check.get()
    x = pos[0]
    y = pos[1]
    # Fill Top, Bot, Left, Right
    # Top
    if x > 0 and scaled_map[x - 1][y] == '.':
        scaled_map[x - 1][y] = 'O'
        points_to_check.put((x - 1, y))
    # Bot
    if x < new_map_height - 1 and scaled_map[x + 1][y] == '.':
        scaled_map[x + 1][y] = 'O'
        points_to_check.put((x + 1, y))
    # Left
    if y > 0 and scaled_map[x][y - 1] == '.':
        scaled_map[x][y - 1] = 'O'
        points_to_check.put((x, y - 1))
    # Right
    if y < new_map_width - 1 and scaled_map[x][y + 1] == '.':
        scaled_map[x][y + 1] = 'O'
        points_to_check.put((x, y + 1))

# Finally, all points that are not filled are the ones where there is not a direct link to an edge
part_2 = 0
for x in range(len(tiles_for_part_2)):
    line = tiles_for_part_2[x]
    for y in range(len(line)):
        current_x = x * 2 + 1
        current_y = y * 2 + 1
        current_pipe = scaled_map[current_x][current_y]
        if current_pipe == '.':
            part_2 += 1


# print(points_to_check.queue)

# print_map(scaled_map)
print("Part 2:", part_2)
