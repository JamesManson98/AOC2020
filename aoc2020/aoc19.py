data = open('aoc2020/input19.txt', 'r').read().split('\n\n')
from itertools import product
rules = data[0].split('\n')
messages = data[1].split('\n')
messages = messages[:-1]

rule_dict = {}
init_inds = []

for rule in rules:
    rule = rule.split(': ')
    key = rule[0]
    if '|' in rule[1]:
        value = rule[1].split(' | ')
    elif '"' in rule[1]:
        value = list(rule[1].strip('"'))
        init_inds.append(key)
    else:
        value = [rule[1]]
    rule_dict[key] = value

# Part 1

def recursive(inds,old_inds):
    old_inds = inds + old_inds
    new_inds = []
    for key in rule_dict.keys():
        if key in old_inds:
            continue
        value = rule_dict[key]
        new_value = []
        for i in range(len(value)):
            n_v = [value[i]]
            for ind in inds:
                if value[i].endswith(' ' + ind) or value[i].startswith(ind + ' ') or (' ' + ind + ' ' in value[i]) or value[i] == ind:
                    n_v_2 = []
                    if value[i].count(ind) == 2:
                        for ind2 in range(len(n_v)):
                            for x in rule_dict[ind]:
                                for y in rule_dict[ind]:
                                    n_v_2.append(n_v[ind2].replace(ind,x,1).replace(ind,y,1))
                        n_v = n_v_2 
                    else:
                        for ind2 in range(len(n_v)):
                            for x in rule_dict[ind]:
                                n_v_2.append(n_v[ind2].replace(ind,x))
                        n_v = n_v_2
            for x in n_v:
                new_value.append(x)
        for ind1 in range(len(new_value)):
            if all(x.isalpha() or x.isspace() for x in new_value[ind1]):
                new_value[ind1] = new_value[ind1].replace(' ', '')
        rule_dict[key] = new_value
        if all(x.isalpha() for x in rule_dict[key]):
            new_inds.append(key)
    if new_inds:
        return recursive(new_inds,old_inds)
    else:
        return rule_dict
        
rule_dict = recursive(init_inds,[])

count = 0
for message in messages:
    if message in rule_dict['0']:
        count += 1
    
print(count)

# Part 2

max_length = len(max(messages, key=len))
useful = []
xs = rule_dict['42']

for i in range(int(max_length/8)):
    last_useful = []
    for message in messages:
        if len(message) > (8*(i+1)-1):
            if message[:8*(i+1)] in xs:
                last_useful.append(message[:8*(i+1)])
                if i > 0:
                    useful.append(message[:8*(i+1)])
    xs = [''.join(p) for p in product(set(last_useful),rule_dict['42'])]  


useful2 = []
xs = rule_dict['31']

for i in range(int(max_length/8)):
    last_useful = []
    for message in messages:
        if len(message) > (8*(i+3)-1):
            if message[-8*(i+1):] in xs:
                useful2.append(message[-8*(i+1):])
                last_useful.append(message[-8*(i+1):])
    xs = [''.join(p) for p in product(rule_dict['31'],set(last_useful))]  

xs = [''.join(p) for p in product(set(useful),set(useful2))]  

valid_messages = []

for message in messages:
    if message in xs:
        count_42 = 0
        count_31 = 0
        for i in range(0,int(len(message)/8)):
            if message[8*i:8*(i+1)] in rule_dict['42']:
                count_42 += 1
            elif message[8*i:8*(i+1)] in rule_dict['31']:
                count_31 += 1
        if count_42 > count_31:
            valid_messages.append(message)
print(len(valid_messages))