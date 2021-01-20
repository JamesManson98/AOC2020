data = open('aoc2020/input2.txt', 'r').read().split('\n')
data = data[:-1]

valid_pass1 = 0
valid_pass2 = 0
for x in data:
    split_pass = x.split(':')
    rule = split_pass[0]
    password = split_pass[1]
    split_rule = rule.split('-')
    i = int(split_rule[0])
    j = int(split_rule[1].split(' ')[0])
    letter = split_rule[1].split(' ')[1]
    if password.count(letter) >= i and password.count(letter) <= j:
        valid_pass1 += 1
    if (password[i] == letter) != (password[j] == letter):
        valid_pass2 += 1
print(valid_pass1)
print(valid_pass2)