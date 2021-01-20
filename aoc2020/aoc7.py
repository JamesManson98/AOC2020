data = open('aoc2020/input7.txt', 'r').read().split('\n')
data = data[:-1]

def recursivesolution1(seen, search, data):
    new_search = []
    for i in range(len(data)):
        split_row = data[i].split(' bags contain ')
        for bag in search:
            if bag in split_row[1]:
                if split_row[0] not in seen:
                    seen.append(split_row[0])
                if split_row[0] not in new_search:
                    new_search.append(split_row[0])
    if new_search == []:
        return len(seen)
    else:
        return recursivesolution1(seen, new_search, data) 

print(recursivesolution1([], ['shiny gold'], data))

def recursivesolution2(counter, search, data):
    new_search = {}
    for i in range(len(data)):
        split_row = data[i].split(' bags contain ')
        bag = split_row[0]
        if (bag not in search) or (split_row[1][:2] == 'no'):
            continue
        else:
            sub_bags_list = split_row[1].split(', ')
            for x in range(len(sub_bags_list)):
                sub_bag_no = int(sub_bags_list[x][0])
                sub_bags_list[x] = sub_bags_list[x][2:]
                sub_bag = sub_bags_list[x].split(' bag')[0]
                try:
                    new_search[sub_bag] += search[bag]*sub_bag_no
                    counter += search[bag]*sub_bag_no
                except:
                    new_search[sub_bag] = search[bag]*sub_bag_no
                    counter += search[bag]*sub_bag_no 
    if new_search == {}:
        return counter
    else:
        return recursivesolution2(counter, new_search, data) 
        
print(recursivesolution2(0, {'shiny gold':1}, data))