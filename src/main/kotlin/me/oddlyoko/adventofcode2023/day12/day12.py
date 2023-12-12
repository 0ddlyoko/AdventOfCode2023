map = [[z.split(" ")[0], [int(y) for y in z.split(" ")[1].split(",")]] for z in open("day12.txt").read().split("\n")]

# I did an over optimization of this challenge.
# The main goal was to reduce the input by setting '#' or '.' where this SHOULD be.
# After more reflection (and loosing ~2h doing that), I decided to not continue to use this optimization, and to resolve the issue like always (bruteforce)

# def force_fill_line_with_pos(line, pos):
#     """
#     Fill the line with values that MUST be at certain position.
#     :return: The new line
#     """
#     new_line = list(line)
#     new_pos = [z for z in pos]
# 
#     def check(the_line, number):
#         the_new_line = [z for z in the_line]
#         the_line_len = len(the_line)
#         # First, check on the LEFT if there is data that SHOULD be at certain position
#         first_left = the_new_line[0:number + 1]
# 
#         first_hash_idx = -1
#         skip = False
#         if '#' in first_left:
#             first_hash_idx = first_left.index('#')
#             # Put data when it's possible
#             hash_to_add = number - first_hash_idx
#             for i in range(hash_to_add):
#                 the_new_line[first_hash_idx + i] = '#'
#             # Put '.' if possible
#             if all(z == '#' for z in the_new_line[first_hash_idx:first_hash_idx + number]):
#                 if first_hash_idx - 1 >= 0:
#                     # fill all left to '.'
#                     for i in range(first_hash_idx):
#                         the_new_line[i] = '.'
#                 # Put '.' on the first
#                 if first_hash_idx + number < the_line_len:
#                     the_new_line[first_hash_idx + number] = '.'
#                 skip = True
#             # Continue as long as it's possible
#             # print("a:", a)
#         return the_new_line, first_hash_idx + number, skip
# 
#     start_from = 0
#     idx = 0
#     while True:
#         if idx >= len(new_pos):
#             break
#         part_of_new_line = new_line[start_from:len(new_line)]
#         the_new_line, last_idx, skip = check(part_of_new_line, new_pos[idx])
#         # It's different. We can change it, and go deeper if needed.
#         if skip:
#             # We can skip this part, as we found it
#             new_line[start_from:start_from+last_idx+1] = []
#             new_pos[idx:idx+1] = []
#             continue
#         if part_of_new_line == the_new_line:
#             break
#         new_line[start_from:start_from+len(the_new_line)] = the_new_line
#         # If it's different, but not full '#', do not continue
#         start_from += last_idx + 1
#         idx += 1
# 
#     # Now, do the same, but starting from the end
#     start_from = 0
#     idx = 0
# 
#     return "".join(new_line), new_pos
# 
# 
# # for line, pos in map[5:]:
# #     force_fill_line_with_pos(line, pos)
# #     break
# # print(force_fill_line_with_pos("???###??#?????", [3, 2, 1]))
# 
# 
# def trim_dots(a):
#     debut = 0
#     fin = len(a)
#     while debut < fin and a[debut] == '.':
#         debut += 1
#     while fin > debut and a[fin - 1] == '.':
#         fin -= 1
#     return a[debut:fin]
# 
# 
# def solve(a, b):
#     arr = trim_dots(a)
#     new_arrangement, pos = force_fill_line_with_pos(arr, b)
#     # Now that we have the new arrangement, first, skip dots
#     # new_arrangement = trim_dots(new_arrangement)
#     print(new_arrangement, pos)
# 
# 
# solve("?#?#?#?#?????#???", [1, 3, 1, 6])


storage = {}


def solve(string, numbers):
    if not numbers and '#' not in string:
        return 1
    if not string or not numbers or len(string) < numbers[0]:
        return 0
    key = (string, ','.join([str(a) for a in numbers]))
    if key in storage:
        return storage[key]
    first_number = numbers[0]
    # Try to put it in first slots
    number_of_possible_combination = 0
    if '.' not in string[:first_number] and (len(string) == first_number or string[first_number] != '#'):
        # It's possible to put it in first slot!
        new_string = string[first_number+1:]
        new_numbers = numbers[1:]
        number_of_possible_combination = solve(new_string, new_numbers)
    # Try to skip first slot
    if string[0] != '#':
        # It's possible to skip first slot!
        new_string = string[1:]
        new_numbers = numbers
        number_of_possible_combination += solve(new_string, new_numbers)
    storage[key] = number_of_possible_combination
    return number_of_possible_combination


part_1 = 0
for m in map:
    a = m[0]
    b = m[1]
    part_1 += solve(a, b)

print("Part 1:", part_1)

part_2 = 0
for m in map:
    a = '?'.join([m[0]] * 5)
    b = m[1] * 5
    part_2 += solve(a, b)

print("Part 2:", part_2)
