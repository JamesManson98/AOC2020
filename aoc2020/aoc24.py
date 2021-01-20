import numpy as np
data = open('aoc2020/input24.txt', 'r').read().split('\n')
data = data[:-1]

tile_dict = {}

for line in data:
    row = 0
    col = 0
    ind = 0
    instructions = []
    while ind < len(line):
        if line[ind] == 'n' or line[ind] == 's':
            instructions.append(line[ind:ind+2])
            ind += 2
        else:
            instructions.append(line[ind])
            ind += 1
    for instr in instructions:
        if instr == 'e':
            col += 2
        elif instr == 'w':
            col -= 2
        elif instr == 'nw':
            col -= 1
            row += 1
        elif instr == 'sw':
            col -= 1
            row -= 1
        elif instr == 'ne':
            col += 1
            row += 1
        elif instr == 'se':
            col += 1
            row -= 1
        else:
            assert False
    try:
        tile_dict[(row,col)] += 1
    except:
        tile_dict[(row,col)] = 1

count = 0

for value in tile_dict.values():
    if value % 2 == 1:
        count += 1

print(count)

for c in range(-110,115):
    for r in range(-65,65):
        try:
            if tile_dict[(r,c)]:
                pass
        except:
            tile_dict[(r,c)] = 0


for i in range(100):
    new_tile_dict = {}

    for key in tile_dict.keys():
        count2 = 0
        (r,c) = key
        neighbour_diff = [(-1,-1), (-1,1), (1,-1), (1,1), (0,2), (0,-2)]
        for (dr,dc) in neighbour_diff:
            neighbour = (r+dr, c+dc)
            try:
                if tile_dict[neighbour] % 2 == 1:
                    count2 += 1
            except:
                continue
        if tile_dict[key] % 2 == 1:
            if count2 == 0 or count2 > 2:
                new_tile_dict[key] = 0
            else:
                new_tile_dict[key] = 1
        else:
            if count2 == 2:
                new_tile_dict[key] = 1
            else:
                new_tile_dict[key] = 0
    tile_dict = new_tile_dict

count1 = 0

for value in new_tile_dict.values():
    if value % 2 == 1:
        count1 += 1

print(count1)