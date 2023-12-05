a = open("day5.txt").read().split("\n\n")
seeds = [int(z) for z in a[0][7:].split(" ")]

b = [(y, [[int(w) for w in x.split(" ")] for x in z.split("\n")[1:]]) for y, z in enumerate(a[1:])]
[z[1].sort(key=lambda l: l[1]) for z in b]

print(b)

min_seed = -1

for seed in seeds:
    current_id = seed
    for i, z in b:
        for y in z:
            if current_id in range(y[1], y[1] + y[2]):
                current_id = y[0] + current_id - y[1]
                break
    if min_seed == -1 or current_id < min_seed:
        min_seed = current_id

print("Part 1:", min_seed)


def get_range_in_range(range_1, range_2):
    """
    Get the range that intersects range_1 and range_2

    :param range_1: The first range
    :param range_2: The second range
    :return: A range that intersects both range
    """
    min_range = max(range_1[0], range_2[0])
    max_range = min(range_1[1], range_2[1])
    if min_range < max_range:
        return [min_range, max_range]
    return False


def get_range_mapped_from_ranges(range, map_of_range):
    """
    From a range, retrieves the mapped range

    :param range:        The range to check
    :param map_of_range: The map of range => range
    :return:
    """
    all_range = []
    all_new_range = []
    for map_range in map_of_range:
        the_range = get_range_in_range(range, [map_range[1], map_range[1] + map_range[2]])
        if the_range:
            all_range.append(the_range)
            range_to_add = map_range[0] - map_range[1]
            all_new_range.append([the_range[0] + range_to_add, the_range[1] + range_to_add])
    # Now, add ranges that are NOT mapped
    not_mapped_range = get_ranges_not_in_range(range, merge_range(all_range))
    all_new_range += not_mapped_range
    return merge_range(all_new_range)


def merge_range(ranges):
    """
    From a list of range, merge it together if we have the same range.
    We sort the initial list

    :param ranges: The range
    :return: A list of range
    """
    ranges.sort(key=lambda lst: lst[0])
    final_ranges = []
    min_range = -1
    max_range = -1
    for range in ranges:
        if min_range == -1:
            min_range = range[0]
            max_range = range[1]
        elif range[0] <= max_range:
            max_range = max(max_range, range[1])
        else:
            final_ranges.append([min_range, max_range])
            min_range = range[0]
            max_range = range[1]
    if min_range != -1:
        final_ranges.append([min_range, max_range])
    return final_ranges


def get_ranges_not_in_range(range, list_of_ranges):
    """
    Returns a list of range that is present in original_list_of_ranges but not in list_of_ranges
    We assume both lists are sorted

    :param range:
    :param list_of_ranges:
    :return:
    """
    result = []

    min_r = range[0]
    max_r = range[1]
    for range in list_of_ranges:
        if min_r < range[0]:
            result.append([min_r, range[0]])
        min_r = max(min_r, range[1])
    if min_r < max_r:
        result.append([min_r, max_r])
    return result


part_2 = -1
for i, seed in enumerate(seeds[::2]):
    seed_ranges = [[seed, seed + seeds[i * 2 + 1]]]
    print(seed_ranges)
    for idx, ranges in b:
        # Transform all seed range into the next seed range
        new_seed_range = []
        for seed_range in seed_ranges:
            result = get_range_mapped_from_ranges(seed_range, ranges)
            new_seed_range.append(result)
        seed_ranges = [a for b in new_seed_range for a in b]
        seed_ranges.sort(key=lambda lst: lst[0])
    print(seed_ranges)

    lowest_number = seed_ranges[0][0]
    if part_2 == -1 or lowest_number < part_2:
        part_2 = lowest_number

print("Part 2:", part_2)
