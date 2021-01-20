data = open('aoc2020/input9.txt', 'r').read().split('\n')
data = data[:-1]

#Part 1

def sums_to(n, l):
    for x in range(len(l)):
        for y in range(len(l)):
            if x == y:
                continue
            else:
                if int(l[x]) + int(l[y]) == int(n):
                    return True
    return False

for ind in range(len(data)):
    if ind<25:
        continue
    else:
        l = data[ind-25:ind]
        tgt = data[ind]
        if not sums_to(tgt, l):
            print(tgt) 
            break

#Part 2

for x in range(len(data)):
    count = 0
    if data[x] == tgt:
        continue
    for y in range(len(data)-x):
        count += int(data[x+y])
        if count == int(tgt):
            c = data[x:x+y+1]
            minimum = float('+inf')
            maximum = float('-inf')
            for z in c:
                if int(z) < minimum:
                    minimum = int(z)
                if int(z) > maximum:
                    maximum = int(z)
            print(minimum+maximum)
        elif count > int(tgt):
            break




