map = [[y for y in z] for z in open("day15.txt").read().split(",")]

part_1 = 0
boxes = [[] for i in range(256)]


def run_hash(label):
    result = 0
    for c in label:
        result += ord(c)
        result *= 17
        result %= 256
    return result


for z in map:
    part_1 += run_hash(z)

print("Part 1:", part_1)


for z in map:
    a = ""
    instruction = '-'
    nbr = 0
    for c in z:
        if instruction == '=':
            nbr *= 10
            nbr += int(c)
        elif c not in ['=', '-']:
            a += c
        else:
            instruction = c
    the_hash = run_hash(a)
    lst = boxes[the_hash]
    found = -1
    for idx, (b_a, b_nbr) in enumerate(lst):
        if a == b_a:
            found = idx
            break
    if instruction == '-':
        if found != -1:
            lst = lst[:found] + lst[found+1:len(lst)]
    else:
        if found != -1:
            lst[found] = (a, nbr)
        else:
            lst.append((a, nbr))
    boxes[the_hash] = lst

part_2 = 0
for box_nbr, box in enumerate(boxes, 1):
    for slot, (a, nbr) in enumerate(box, 1):
        part_2 += box_nbr * slot * nbr

print("Part 2:", part_2)
