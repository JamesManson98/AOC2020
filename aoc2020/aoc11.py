data = open('aoc2020/input11.txt', 'r').read().split('\n')
data = data[:-1]

# Part 1:

def iteration(data):
    new_data = data.copy()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '.':
                continue
            else:
                count = 0
                for y1 in range(y-1,y+2):
                    for x1 in range(x-1,x+2):
                        if (x1 == x and y1 == y) or (x1 > len(data[y])-1) or (y1 > len(data)-1) or (x1 < 0) or (y1 < 0):
                            continue
                        elif data[y1][x1] == '#':
                            count += 1
                if data[y][x] == 'L' and count == 0:
                    if len(data[y]) - 1 > x > 0:
                        new_data[y] = new_data[y][:x] + '#' + new_data[y][x+1:]
                    elif len(data[y]) - 2 < x:
                        new_data[y] = new_data[y][:x] + '#'
                    elif x == 0:
                        new_data[y] = '#' + new_data[y][x+1:]
                elif data[y][x] == '#' and count > 3:
                    if len(data[y]) - 1 > x > 0:
                        new_data[y] = new_data[y][:x] + 'L' + new_data[y][x+1:]
                    elif len(data[y]) - 2 < x:
                        new_data[y] = new_data[y][:x] + 'L'
                    elif x == 0:
                        new_data[y] = 'L' + new_data[y][x+1:]
    return new_data

def recursion(data):
    new_data = iteration(data)
    if data != new_data:
        return recursion(new_data)
    else:
        return new_data

def seats_count(data):
    count = 0
    for row in data:
        count += row.count('#')    
    return count            

print(seats_count(recursion(data)))

# Part 2:

def iteration2(data):
    new_data = data.copy()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '.':
                continue
            else:
                count = 0
                for y1 in range(y-1,y+2):
                    for x1 in range(x-1,x+2):
                        if (x1 == x and y1 == y) or (x1 > len(data[y])-1) or (y1 > len(data)-1) or (x1 < 0) or (y1 < 0):
                            continue
                        elif data[y1][x1] == '#':
                            count += 1
                        elif data[y1][x1] == '.':
                            a = y1 - y
                            b = x1 - x
                            y2 = y1 + a
                            x2 = x1 + b
                            if not (-1 < y2 < len(data[y]) and -1 < x2 < len(data[x])):
                                continue
                            elif data[y2][x2] == '.':
                                while data[y2][x2] == '.' and -1 < y2+a < len(data[y]) and -1 < x2+b < len(data[x]):
                                    y2 += a
                                    x2 += b
                                    if data[y2][x2] == '#':
                                        count += 1
                            elif data[y2][x2] == '#':
                                count += 1
                if data[y][x] == 'L' and count == 0:
                    if len(data[y]) - 1 > x > 0:
                        new_data[y] = new_data[y][:x] + '#' + new_data[y][x+1:]
                    elif len(data[y]) - 2 < x:
                        new_data[y] = new_data[y][:x] + '#'
                    elif x == 0:
                        new_data[y] = '#' + new_data[y][x+1:]
                elif data[y][x] == '#' and count > 4:
                    if len(data[y]) - 1 > x > 0:
                        new_data[y] = new_data[y][:x] + 'L' + new_data[y][x+1:]
                    elif len(data[y]) - 2 < x:
                        new_data[y] = new_data[y][:x] + 'L'
                    elif x == 0:
                        new_data[y] = 'L' + new_data[y][x+1:]
    return new_data

def recursion2(data):
    new_data = iteration2(data)
    if data != new_data:
        return recursion2(new_data)
    else:
        return new_data

print(seats_count(recursion2(data)))
