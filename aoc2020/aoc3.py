data = open('aoc2020/input3.txt', 'r').read().split('\n')
data = data[:-1]

totaltrees = 1
width = len(data[0])

for (dr,dc) in [(1,1),(1,3),(1,5),(1,7),(2,1)]:
    (r,c) = (0,0)
    treecount = 0
    while r < len(data):
        if data[r][c%width] == '#':
            treecount += 1
        r += dr
        c += dc
    totaltrees *= treecount
    if (dr,dc) == (1,3):
        print(treecount)

print(totaltrees)