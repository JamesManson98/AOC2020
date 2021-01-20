import numpy as np
data = open('aoc2020/input17.txt', 'r').read().split('\n')
data = data[:-1]

# Part 1

x_len = len(data[0])
y_len = len(data)
z_len = 1
array = np.empty([z_len, y_len, x_len], dtype = str)
for y in range(len(data)):
    for x, d in enumerate(data[y]):
        array[0][y][x] = d

for i in range(6):
    counter = 0
    new_array = np.empty([z_len+2, y_len+2, x_len+2], dtype = str)
    for x in range(x_len+2):
        for y in range(y_len+2):
            for z in range(z_len+2):
                count = 0 
                for x1 in range(x-2,x+1):
                    for y1 in range(y-2,y+1):
                        for z1 in range(z-2,z+1):
                            if (0 <= x1 < x_len) and (0 <= y1 < y_len) and (0 <= z1 < z_len) and not (x1 == x-1 and y1 == y-1 and z1 == z-1):
                                if array[z1][y1][x1] == '#':
                                    count += 1
                if (0 < x <= x_len) and (0 < y <= y_len) and (0 < z <= z_len):
                    if array[z-1][y-1][x-1] == '#':
                        if count == 2 or count == 3:
                            new_array[z][y][x] = '#'
                        else:
                            new_array[z][y][x] = '.'
                    elif count == 3:
                        new_array[z][y][x] = '#'
                    else:
                        new_array[z][y][x] = '.'
                elif count == 3:
                    new_array[z][y][x] = '#'
                else:
                    new_array[z][y][x] = '.'
                if new_array[z][y][x] == '#':
                    counter += 1
    array = new_array
    x_len += 2
    y_len += 2
    z_len += 2

print(counter)

# Part 2

w_len = 1
x_len = len(data[0])
y_len = len(data)
z_len = 1
array = np.empty([w_len, z_len, y_len, x_len], dtype = str)
for y in range(len(data)):
    for x, d in enumerate(data[y]):
        array[0][0][y][x] = d

for i in range(6):
    counter = 0
    new_array = np.empty([w_len+2, z_len+2, y_len+2, x_len+2], dtype = str)
    for x in range(x_len+2):
        for y in range(y_len+2):
            for z in range(z_len+2):
                for w in range(w_len+2):
                    count = 0 
                    for x1 in range(x-2,x+1):
                        for y1 in range(y-2,y+1):
                            for z1 in range(z-2,z+1):
                                for w1 in range(w-2,w+1):
                                    if (0 <= x1 < x_len) and (0 <= y1 < y_len) and (0 <= z1 < z_len) and (0 <= w1 < w_len) and not (w1 == w-1 and x1 == x-1 and y1 == y-1 and z1 == z-1):
                                        if array[w1][z1][y1][x1] == '#':
                                            count += 1
                    if (0 < x <= x_len) and (0 < y <= y_len) and (0 < z <= z_len) and (0 < w <= w_len):
                        if array[w-1][z-1][y-1][x-1] == '#':
                            if count == 2 or count == 3:
                                new_array[w][z][y][x] = '#'
                            else:
                                new_array[w][z][y][x] = '.'
                        elif count == 3:
                            new_array[w][z][y][x] = '#'
                        else:
                            new_array[w][z][y][x] = '.'
                    elif count == 3:
                        new_array[w][z][y][x] = '#'
                    else:
                        new_array[w][z][y][x] = '.'
                    if new_array[w][z][y][x] == '#':
                        counter += 1
    array = new_array
    w_len += 2
    x_len += 2
    y_len += 2
    z_len += 2

print(counter)


