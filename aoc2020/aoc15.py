nos = [18,11,9,0,5,1]
dict_nos = {}

for ind, n in enumerate(nos):
    dict_nos[n] = ind + 1

count = len(nos)
last = nos[-1]

for count_max in [2020,30000000]:
    while count < count_max:
        try:
            last_ind = dict_nos[last]
            dict_nos[last] = count       
            last = count - last_ind
        except:
            dict_nos[last] = count
            last = 0
        count += 1
    print(last)