data = open('aoc2020/input21.txt', 'r').read().split('\n')
data = data[:-1]

allergen_list = []
ingredient_list = []


for line in data:
    spl_line = line.split(' (contains ')
    contains = spl_line[1].strip(')')
    contains = contains.split(', ')
    ingredients = spl_line[0].split()
    for allergen in contains:
        if allergen not in allergen_list:
            allergen_list.append(allergen)
    for ingredient in ingredients:
        if ingredient not in ingredient_list:
            ingredient_list.append(ingredient)

maybe_allergen = []
allergen_dict = {}

for allergen in allergen_list:
    poss = []
    intersection_set = set()
    for line in data:
        spl_line = line.split(' (contains ')
        contains = spl_line[1].strip(')')
        contains = contains.split(', ')
        ingredients = spl_line[0].split()
        if allergen in contains:
            if intersection_set == set():
                intersection_set = set(ingredients)
            else:
                intersection_set = intersection_set.intersection(ingredients)
    for ingredient in list(intersection_set):
        poss.append(ingredient)
        if ingredient not in maybe_allergen:
            maybe_allergen.append(ingredient)
    allergen_dict[allergen] = poss

not_allergen = ingredient_list
for ingredient in maybe_allergen:
    not_allergen.remove(ingredient)

count = 0
for ingredient in not_allergen:
    for line in data:
        spl_line = line.split(' (contains ')
        ingredients = spl_line[0].split()
        count += ingredients.count(ingredient)

allergen_dict2 = {}
while True:
    for allergen in sorted(allergen_dict.keys()):
        if len(allergen_dict[allergen]) == 1:
            ingredient = allergen_dict[allergen][0]
            allergen_dict2[allergen] = ingredient
            for allergen2 in sorted(allergen_dict.keys()):
                if ingredient in allergen_dict[allergen2]:
                    allergen_dict[allergen2].remove(ingredient)
    if len(allergen_dict2.keys()) == len(allergen_dict.keys()):
        break
        
ans = ''

for allergen in sorted(allergen_dict2.keys()):
    ans += allergen_dict2[allergen] + ','
ans = ans.strip(',')

print(count)
print(ans)