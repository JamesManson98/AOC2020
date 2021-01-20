import numpy as np
data = open('aoc2020/input12.txt', 'r').read().split('\n')
data = data[:-1]

# Part 1
ind = 1
x = 0
y = 0

for r in data:
    if r[0] == 'R':
        ind = int((ind + (int(r[1:])/90))%4)
    elif r[0] == 'L':
        ind = int((ind - (int(r[1:])/90))%4)
    elif r[0] == 'F':
        if ind == 0:
            y += int(r[1:])
        elif ind == 1:
            x += int(r[1:])
        elif ind == 2:
            y -= int(r[1:])
        elif ind == 3:
            x -= int(r[1:])
    elif r[0] == 'N':
        y += int(r[1:])
    elif r[0] == 'E':
        x += int(r[1:])
    elif r[0] == 'S':
        y -= int(r[1:])
    elif r[0] == 'W':
        x -= int(r[1:])
print(abs(x)+abs(y))

# Part 2

wp = [10, 1]
x = 0
y = 0

for r in data:
    if r[0] == 'L':
        wp = [int(round(-wp[1]*np.sin(np.pi*int(r[1:])/180) + wp[0]*np.cos(np.pi*int(r[1:])/180))), int(round(wp[1]*np.cos(np.pi*int(r[1:])/180) + wp[0]*np.sin(np.pi*int(r[1:])/180)))]
    elif r[0] == 'R':
        wp = [int(round(-wp[1]*np.sin(-np.pi*int(r[1:])/180) + wp[0]*np.cos(-np.pi*int(r[1:])/180))), int(round(wp[1]*np.cos(-np.pi*int(r[1:])/180) + wp[0]*np.sin(-np.pi*int(r[1:])/180)))]
    elif r[0] == 'F':
        x += int(r[1:])*wp[0]
        y += int(r[1:])*wp[1]
    elif r[0] == 'N':
        wp[1] += int(r[1:])
    elif r[0] == 'E':
        wp[0] += int(r[1:])
    elif r[0] == 'S':
        wp[1] -= int(r[1:])
    elif r[0] == 'W':
        wp[0] -= int(r[1:])
print(abs(x)+abs(y))