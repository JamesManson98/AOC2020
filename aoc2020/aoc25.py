data = open('aoc2020/input25.txt', 'r').read().split('\n')
data = data[:-1]
card_key = int(data[0])
door_key = int(data[1])

def find_loop_size(value, SN):
    product = 1
    loop_size = 0
    while product != value:
        product *= SN
        product %= 20201227
        loop_size += 1
    return loop_size

def transform(loop_size, SN):
    product = 1
    for _ in range(loop_size):
        product *= SN
        product %= 20201227
    return product

loop_size = find_loop_size(card_key, 7)
print(transform(loop_size, door_key))