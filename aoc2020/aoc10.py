data = open('aoc2020/input10.txt', 'r').read().split('\n')
data = data[:-1]

int_list = []

for x in data:
    int_list.append(int(x))
int_list.append(0)
int_list.append(max(int_list)+3)

# Part 1

int_list.sort()

count_1 = 0
count_3 = 0

for ind in range(len(int_list)):
    if int_list[ind] - int_list[ind-1] == 1:
        count_1 += 1
    elif int_list[ind] -int_list[ind-1] == 3:
        count_3 += 1

print(count_1*count_3)

# Part 2

combs = []

for g in range(len(int_list)):
    if g == 0:
        combs.append(1)
    elif g == 1:
        if int_list[g] - int_list[g-1] < 4:
            combs.append(1)
    elif g == 2:
        if int_list[g] - int_list[g-2] < 4:
            combs.append(combs[g-1]+combs[g-2])
        else:
            combs.append(combs[g-1])
    else:
        if int_list[g] - int_list[g-3] < 4:
            combs.append(combs[g-1]+combs[g-2]+combs[g-3])
        elif int_list[g] - int_list[g-2] < 4:
            combs.append(combs[g-1]+combs[g-2])
        else:
            combs.append(combs[g-1])
print(combs[-1])