data = open('aoc2020/input1.txt', 'r').read().split('\n')
data = data[:-1]

def sumto2020(data):
    for number1 in data:
        for number2 in data:
            if int(number1) + int(number2) == 2020:
                return (int(number1)*int(number2))
print(sumto2020(data))

def sumto2020_3(data):
    for number1 in data:
        for number2 in data:
            for number3 in data:
                if int(number1) + int(number2) + int(number3) == 2020:
                    return (int(number1)*int(number2)*int(number3))
print(sumto2020_3(data))