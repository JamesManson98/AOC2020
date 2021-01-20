data = open('aoc2020/input22.txt', 'r').read().split('\n\n')
from copy import deepcopy

P1 = data[0].split('\n')
P2 = data[1].split('\n')
P1 = P1[1:]
P2 = P2[1:-1]

while True:
    card1 = P1.pop(0)
    card2 = P2.pop(0)
    if int(card1) > int(card2):
        P1.append(card1)
        P1.append(card2)
    elif int(card1) < int(card2):
        P2.append(card2)
        P2.append(card1)
    else:
        assert False
    if len(P1) == 0 or len(P2) == 0:
        break 

if len(P1) != 0:
    winner = P1
else:
    winner = P2

score = 0

for i in range(len(winner)):
    score += (len(winner)-i)*int(winner[i])

print(score)

# Part 2:

def recursive(P1, P2, Prev):
    while True:
        card1 = P1.pop(0)
        card2 = P2.pop(0)
        if int(card1) > len(P1) or int(card2) > len(P2):
            if int(card1) > int(card2):
                P1.append(card1)
                P1.append(card2)
            elif int(card1) < int(card2):
                P2.append(card2)
                P2.append(card1)
            else:
                assert False
        else:
            Prev_1 = [deepcopy(P1[:int(card1)]), deepcopy(P2[:int(card2)])]
            _, _, winner = recursive(P1[:int(card1)], P2[:int(card2)], Prev_1)
            if winner == 'P1':
                P1.append(card1)
                P1.append(card2)
            elif winner == 'P2':
                P2.append(card2)
                P2.append(card1)
            else:
                assert False
        if [P1, P2] in Prev:
            return P1, P2, 'P1'
        Prev.append([deepcopy(P1), deepcopy(P2)])
        if len(P1) == 0:
            return P1, P2, 'P2'
        elif len(P2) == 0:
            return P1, P2, 'P1'

P1 = data[0].split('\n')
P2 = data[1].split('\n')
P1 = P1[1:]
P2 = P2[1:-1]

Prev = [deepcopy(P1), deepcopy(P2)]

P1, P2, winner = recursive(P1,P2,Prev)

if winner == 'P1':
    winner = P1
elif winner == 'P2':
    winner = P2

score = 0

for i in range(len(winner)):
    score += (len(winner)-i)*int(winner[i])

print(score)  
