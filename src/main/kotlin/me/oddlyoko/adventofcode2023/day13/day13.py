map = [[y for y in z.split('\n')] for z in open("day13.txt").read().split("\n\n")]

part_1 = 0
part_2 = 0

for z in map:
    part_1_done = False
    part_2_done = False
    # Check cols
    for i in range(len(z[0]) - 1):
        b = [a[i] for a in z]
        c = [a[i + 1] for a in z]
        is_diff_part_2_a = False
        if b != c:
            # Check if there is one diff
            f = [i for i in range(len(b)) if b[i] != c[i]]
            if len(f) == 1:
                # We can take this one
                is_diff_part_2_a = True
        if is_diff_part_2_a or b == c:
            # Found it at pos = i
            # Check if it's a perfect one
            perfect = not is_diff_part_2_a
            perfect_part_2 = is_diff_part_2_a
            is_diff_part_2 = is_diff_part_2_a
            for j in range(1, i + 1):
                if i + j + 1 >= len(z[0]):
                    break
                d = [a[i - j] for a in z]
                e = [a[i + 1 + j] for a in z]
                if d != e:
                    perfect = False
                    # If there is only one diff, we can skip this line as long as there is no diff for the next ones
                    if is_diff_part_2:
                        perfect_part_2 = False
                    else:
                        f = [i for i in range(len(d)) if d[i] != e[i]]
                        is_diff_part_2 = True
                        perfect_part_2 = len(f) == 1
            if perfect and not part_1_done:
                part_1 += i + 1
                part_1_done = True
            if perfect_part_2 and not part_2_done:
                part_2 += i + 1
                part_2_done = True
    # part_1_done = False
    # part_2_done = False
    # Check rows
    for i in range(len(z) - 1):
        b = z[i]
        c = z[i + 1]
        is_diff_part_2_a = False
        if b != c:
            # Check if there is one diff
            f = [i for i in range(len(b)) if b[i] != c[i]]
            if len(f) == 1:
                # We can take this one
                is_diff_part_2_a = True
        if is_diff_part_2_a or b == c:
            # Found it at pos = i
            # Check if it's a perfect one
            perfect = not is_diff_part_2_a
            perfect_part_2 = is_diff_part_2_a
            is_diff_part_2 = is_diff_part_2_a
            for j in range(1, i + 1):
                if i + j + 1 >= len(z):
                    break
                d = z[i - j]
                e = z[i + 1 + j]
                if d != e:
                    perfect = False
                    # If there is only one diff, we can skip this line as long as there is no diff for the next ones
                    if is_diff_part_2:
                        perfect_part_2 = False
                    else:
                        f = [i for i in range(len(d)) if d[i] != e[i]]
                        is_diff_part_2 = True
                        perfect_part_2 = len(f) == 1
            if perfect and not part_1_done:
                part_1 += (i + 1) * 100
                part_1_done = True
            if perfect_part_2 and part_2_done:
                print("Found another new line!")
                pass
            if perfect_part_2 and not part_2_done:
                part_2 += (i + 1) * 100
                part_2_done = True

print("Part 1:", part_1)
print("Part 2:", part_2)
