data = open('aoc2020/input4.txt', 'r').read().split('\n\n')

valid1 = 0
valid2 = 0
for row in data:
    if all(field in row for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl','ecl', 'pid']):
        valid1 += 1

        passport = {}
        current_valid = True
        fields = row.split()
        for field in fields:
            k, v = field.split(':')
            passport[k] = v 
        byr = passport['byr']
        iyr = passport['iyr']
        eyr = passport['eyr']
        hgt = passport['hgt']
        hcl = passport['hcl']
        ecl = passport['ecl']
        pid = passport['pid']

        if 1920 > int(byr) or 2002 < int(byr):
            current_valid = False

        if 2010 > int(iyr) or 2020 < int(iyr):
            current_valid = False

        if 2020 > int(eyr) or 2030 < int(eyr):
            current_valid = False    

        if 'cm' not in hgt and 'in' not in hgt:
            current_valid = False
        elif 'cm' in hgt:
            hgt_num = hgt[:-2]
            if int(hgt_num) < 150 or int(hgt_num) > 193:
                current_valid = False
        elif 'in' in hgt:
            hgt_num = hgt[:-2]
            if int(hgt_num) < 59 or int(hgt_num) > 76:
                current_valid = False

        if hcl[0] == '#':
            hcl_allowed = "0123456789abcdef"
            if not all(c in hcl_allowed for c in hcl[1:]) or len(hcl)!=7:
                current_valid = False
        else:
            current_valid = False

        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            current_valid = False

        pid_allowed = "0123456789"
        if not all(c in pid_allowed for c in pid) or len(pid)!=9:
            current_valid = False

        valid2 += current_valid
        
print(valid1)
print(valid2)

