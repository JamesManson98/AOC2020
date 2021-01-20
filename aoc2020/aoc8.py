data = open('aoc2020/input8.txt', 'r').read().split('\n')
data = data[:-1]

#Part 1

acc = 0
inds_visited = []
ind = 0

while ind < len(data):
    instr = data[ind].split(' ')
    inds_visited.append(ind)
    if len(set(inds_visited)) != len(inds_visited):
        break
    if instr[0] == 'acc':
        acc += int(instr[1])
        ind += 1
    elif instr[0] == 'jmp':
        ind += int(instr[1])
    elif instr[0] == 'nop':
        ind += 1

print(acc)

#Part 2

def troubleshoot(data):
    acc = 0
    inds_visited = []
    ind = 0
    while ind < len(data):
        instr = data[ind].split(' ')
        inds_visited.append(ind)
        if len(set(inds_visited)) != len(inds_visited):
            return False, acc
        if instr[0] == 'acc':
            acc += int(instr[1])
            ind += 1
        elif instr[0] == 'jmp':
            ind += int(instr[1])
        elif instr[0] == 'nop':
            ind += 1
    return True, acc

for i in range(len(data)):
    data_copy = data.copy()
    instruct = data[i].split(' ')
    if instruct[0] == 'acc':
        continue
    elif instruct[0] == 'jmp':
        data_copy[i] = 'nop ' + instruct[1]
    elif instruct[0] == 'nop':
        data_copy[i] = 'jmp ' + instruct[1]
    (x, y) = troubleshoot(data_copy)
    if x:
        print(y)