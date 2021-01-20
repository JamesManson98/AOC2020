from more_itertools import locate
data = open('aoc2020/input18.txt', 'r').read().split('\n')
data = data[:-1]

def counter(string):
    count = 0
    count_list = []
    for x in string:
        if x == '(':
            count += 1
        if x == ')':
            count -= 1
        count_list.append(count)
    return count_list

def evaluate(string):
    result = None
    string = string.split()
    for ind, x in enumerate(string):
        if x == '+' and result == None:
            result = int(string[ind-1]) + int(string[ind+1])
        elif x == '*' and result == None:
            result = int(string[ind-1]) * int(string[ind+1])
        elif x == '+':
            result += int(string[ind+1])
        elif x == '*':
            result *= int(string[ind+1])
    return str(result)

def evaluate2(string):
    if '*' not in string:
        return str(eval(string))
    elif '+' not in string:
        return str(eval(string))
    else:
        sub_strings = string.split(' * ')
        for sub_string in sub_strings:
            if '+' in sub_string:
                string = string.replace(sub_string, str(eval(sub_string)))
        return evaluate2(string)

for P in ['P1','P2']:
    ans = 0
    for string in data:
        while '(' in string:
            counts = counter(string)
            max_count = max(counts)
            inds = list(locate(counts, lambda a: a == max_count))
            new_inds = inds.copy()
            for ind in inds.copy():
                if (ind - 1 in new_inds) and (ind + 1 in new_inds):
                    inds.remove(ind)
            inds.reverse()
            for i in range(1,len(inds),2):
                sub_str = string[inds[i]+1:inds[i-1]+1]
                if P == 'P1':
                    ev = evaluate(sub_str)
                elif P == 'P2':
                    ev = evaluate2(sub_str)
                sub_str_br = string[inds[i]:inds[i-1]+2]
                string = string.replace(sub_str_br,ev)


        if '+' in string or '*' in string:
            if P == 'P1':
                string = evaluate(string)
            elif P == 'P2':
                string = evaluate2(string)
        ans += int(string)
    print(ans)