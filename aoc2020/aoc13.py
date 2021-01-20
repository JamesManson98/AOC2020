data = open('aoc2020/input13.txt', 'r').read().split('\n')
data = data[:-1]
min_time = int(data[0])
buses = data[1].split(',')

# Part 1

while 'x' in buses:
    buses.remove('x')
for ind in range(len(buses)):
    buses[ind] = int(buses[ind])


time = min_time
found = False

while found == False:
    for bus in buses:
        if time % bus == 0:
            first_time = time
            found = True
            break
    time += 1

print(bus*(first_time-min_time))

# Part 2

found = False
buses_x = data[1].split(',')
inds = []
buses.sort(reverse=True)

for bus in buses:    
    ind = buses_x.index(str(bus))
    inds.append(ind)

time = inds[0]
multiplier = 1

for ind in range(0,len(buses)):
    while found == False:
        if (time + inds[ind]) % buses[ind] == 0:
            multiplier *= buses[ind]
            break
        time += multiplier
print(time)