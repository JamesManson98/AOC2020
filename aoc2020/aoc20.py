data = open('aoc2020/input20.txt', 'r').read().split('\n\n')
data = data[:-1]
import numpy as np

def flip(lines):
    ans = []
    for line in lines:
        ans.append(''.join(line[::-1]))
    return ans

def rotate(lines):
    ans = []
    for i in range(len(lines)):
        row = ''
        for j in range(len(lines)-1,-1,-1):
            row += lines[j][i]
        ans.append(row)
    return ans

def get_edges(lines):
    left = ''
    right = ''
    for line in lines:
        left += line[0]
        right += line[-1]
    return lines[0], right, lines[-1], left  # TOP, RIGHT, BOTTOM, LEFT

def unmatched(tile, i_s, ind_unmatched):
    for i in i_s:
        indices = []
        tile_edges = get_edges(tile_poss[tile][i])
        for ind, edge in enumerate(tile_edges):
            match = False
            for tile2 in tile_nos:
                    if tile == tile2:
                        continue
                    else:
                        for j in range(8):
                            if edge == tile_poss[tile2][j][0]:
                                match = True
            if not match:
                indices.append(ind)
        if indices == ind_unmatched:
            return i

def remove_borders(tile):
    new_tile = []
    for ind in range(1,len(tile)-1):
        new_tile.append(tile[ind][1:-1])
    return new_tile

tile_poss = {}
tile_nos = []

for tile in data:
    all_poss = []
    tile_no = tile.split('\n')[0].strip(':').strip('Tile ')
    tile_nos.append(tile_no)
    lines = tile.split('\n')[1:]
    for i in range(4):
        for j in range(2):
            all_poss.append(lines)
            lines = flip(lines)
        lines = rotate(lines)
    tile_poss[tile_no] = all_poss

for tile1 in tile_nos:
    count = 0
    for edge in get_edges(tile_poss[tile1][0]):   
        indices = []
        match = False
        for tile2 in tile_nos:
            if tile1 == tile2:
                continue
            else:
                for j in [0,4]:
                    if edge in get_edges(tile_poss[tile2][j]):
                        match = True
        if match:
            count += 1
    if count < 3: 
        sample_corner_tile = tile1

tleft_i = unmatched(sample_corner_tile, [0,1,2,3,4,5,6,7], [0,3])

# Completing top row

orientation_dict = {sample_corner_tile: tleft_i}
sample_corner_tile[tleft_i]
grid = np.empty([12,12], dtype = "<U10") # Grid (r,c)
grid[0][0] = sample_corner_tile
curr_tile = sample_corner_tile
for i in range(1,12):
    js = []
    match = False
    orientation = orientation_dict[curr_tile]
    _, right, _, _ = get_edges(tile_poss[curr_tile][orientation])
    for tile in tile_nos:
        if tile == curr_tile:
            continue
        else:
            for j in range(8):
                _, _, _, left = get_edges(tile_poss[tile][j])
                if right == left:
                    match = True
                    js.append(j)
        if match:
            break
    orientation_dict[tile] = js[0]
    grid[0][i] = tile
    curr_tile = tile

# Completing rest of the puzzle

for idx, curr_tile in enumerate(grid[0]):
    for i in range(1,12):
        js = []
        match = False
        orientation = orientation_dict[curr_tile]
        _, _, bottom, _ = get_edges(tile_poss[curr_tile][orientation])
        for tile in tile_nos:
            if tile == curr_tile:
                continue
            else:
                for j in range(8):
                    top, _, _, _ = get_edges(tile_poss[tile][j])
                    if top == bottom:
                        match = True
                        js.append(j)
            if match:
                break
        orientation_dict[tile] = js[0]
        grid[i][idx] = tile
        curr_tile = tile

#Assembling the puzzle:
removed_borders = {}

for r, row in enumerate(grid):
    for c, column in enumerate(grid[r]):
        tile_no = grid[r][c]
        orientation = orientation_dict[tile_no]
        tile = tile_poss[tile_no][orientation]
        tile = remove_borders(tile)
        removed_borders[tile_no] = tile

picture = []
for r, row in enumerate(grid):
    for ind in range(8):
        temp = ''
        for c, column in enumerate(grid[r]):
            temp += removed_borders[grid[r][c]][ind]
        picture.append(temp)

sea_monsters = 0
count = 0

all_poss = []
for i in range(4):
    for j in range(2):
        all_poss.append(picture)
        picture = flip(picture)
    picture = rotate(picture)


for i, picture in enumerate(all_poss):
    for idx, line in enumerate(picture[1:-1], start = 1):
        prev_line = picture[idx-1]
        next_line = picture[idx+1]
        for ind in range(len(line)):
            try:
                if line[ind] == '#' and line[ind+5:ind+7] == '##' and line[ind+11:ind+13] == '##' and line[ind+17:ind+20] == '###' and prev_line[ind+18] == '#' and next_line[ind+1] == '#' and next_line[ind+4] == '#' and next_line[ind+7] == '#' and next_line[ind+10] == '#' and next_line[ind+13] == '#' and next_line[ind+16] == '#':
                            sea_monsters += 1
            except:
                continue

for line in picture:
    for ind in range(len(line)):
        if line[ind] == '#':
            count += 1

print(int(grid[0][0])*int(grid[0][11])*int(grid[11][0])*int(grid[11][11]))
print(count-sea_monsters*15)
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   