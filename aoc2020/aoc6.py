data = open('aoc2020/input6.txt', 'r').read().split('\n\n')
data[-1] = data[-1][:-1]

# Part 1

count = 0
for form in data:
    form = form.replace("\n", "")
    count += len(set(form))

# Part 2

count2 = 0
for form2 in data:
    form2 = form2.split('\n')
    alph = set(form2[0])
    for x in form2:
        for i in alph.copy():
            if i not in x:
                alph.remove(i)
    count2 += len(set(alph))

print(count)
print(count2)
