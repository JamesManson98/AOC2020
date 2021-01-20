data = open('aoc2020/input16.txt', 'r').read().split('\n\n')
fields = data[0].split('\n')
my_ticket = data[1].split('\n')
nearby = data[2].split('\n')
my_ticket = my_ticket[1:]
nearby = nearby[1:-1]

minimum = float('inf')
maximum = float('-inf')
field_names = []
value_ranges = []
for field in fields:
    if '-' in field:
        split_f = field.split(': ')
        field_names.append(split_f[0])
        value_ranges.append(split_f[1])       
        values = split_f[1].split(' or ')
        if minimum > int(values[0][:2]):
            minimum = int(values[0][:2])
        if maximum < int(values[1][4:]):
            maximum = int(values[1][4:])

invalid = 0
valid_tickets = []
for ticket in nearby:
    valid = True
    split_ticket = ticket.split(',')
    for value in split_ticket:
        if not (minimum <= int(value) <= maximum):
            invalid += int(value)
            valid = False
            break
    if valid:
        valid_tickets.append(ticket)
    
print(invalid)


# Part 2
poss_inds = {}
ans = 1
for x in range(len(field_names)):
    possible_inds = []
    max_min_v = value_ranges[x].split(' or ')
    maximum_1 = max_min_v[0].split('-')[1]
    maximum_2 = max_min_v[1].split('-')[1]
    minimum_1 = max_min_v[0].split('-')[0]
    minimum_2 = max_min_v[1].split('-')[0]
    for ind in range(len(split_ticket)):
        correct_ind = True
        for ticket in valid_tickets: 
            split_ticket = ticket.split(',')
            if not (int(minimum_1) <= int(split_ticket[ind]) <= int(maximum_1) or int(minimum_2) <= int(split_ticket[ind]) <= int(maximum_2)):
                correct_ind = False
                break
        if correct_ind:
            possible_inds.append(ind)
    poss_inds[field_names[x]] = possible_inds

a = sum(1 for v in poss_inds.values() if len(v) > 1)
while a>0:
    for field in poss_inds:
        if len(poss_inds[field]) == 1:
            for f2 in poss_inds:
                if f2 == field:
                    continue
                elif poss_inds[field][0] in poss_inds[f2]:
                    poss_inds[f2].remove(poss_inds[field][0])
    a = sum(1 for v in poss_inds.values() if len(v) > 1)

for keys in poss_inds:
    if 'departure' in keys:
        my_split_ticket = my_ticket[0].split(',')
        ans *= int(my_split_ticket[poss_inds[keys][0]])

print(ans)

