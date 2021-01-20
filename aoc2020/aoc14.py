data = open('aoc2020/input14.txt', 'r').read().split('\n')
data = data[:-1]

# Part 1

def encode(mask, enc):
    mask = list(mask)
    for ind in range(len(enc)):
        if mask[len(mask)-(len(enc)-ind)] == 'X':
            mask[len(mask)-(len(enc)-ind)] = enc[ind]
    for ind2 in range(len(mask)):
        if mask[ind2] == 'X':
            mask[ind2] = '0'
    mask = ''.join(mask)
    return mask

mem = {}
for line in data:
    if 'mask' in line:
        mask = line[7:]
    elif 'mem' in line:
        spl_line = line.split(' = ')
        enc = bin(int(spl_line[1]))[2:]
        encoded = encode(mask,enc)
        address = int(spl_line[0][4:-1])
        mem[address] = int(encoded,2)
print(sum(mem.values()))

# Part 2

def mask_recursion(masks):
    new_masks = []
    for mask in masks:
        if 'X' in mask:
            mask = list(mask)
            ind = mask.index('X')
            mask[ind] = '0'
            new_masks.append(''.join(mask))
            mask[ind] = '1'
            new_masks.append(''.join(mask))
        else:
            return masks
    return mask_recursion(new_masks)


def encode2(mask, enc):
    mask = list(mask)
    for ind in range(len(enc)):
        if mask[len(mask)-(len(enc)-ind)] == '0':
            mask[len(mask)-(len(enc)-ind)] = enc[ind]
    mask = ''.join(mask)
    return mask_recursion([mask])

mem = {}
for line in data:
    if 'mask' in line:
        mask = line[7:]
    elif 'mem' in line:
        spl_line = line.split(' = ')
        adr = bin(int(spl_line[0][4:-1]))[2:]
        enc_adr = encode2(mask,adr)
        for x in enc_adr:       
            mem[int(x,2)] = int(spl_line[1])
print(sum(mem.values()))