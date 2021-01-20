data = open('aoc2020/input5.txt', 'r').read()
data = data.replace('F','0')
data = data.replace('B','1')
data = data.replace('R','1')
data = data.replace('L','0')
data = data.split('\n')
data = data[:-1]

seat_ids = []
highest_id = float('-inf')

for seat in data:
    seat_id = int(seat, 2)
    seat_ids.append(seat_id)
    if seat_id > highest_id:
        highest_id = seat_id

for i in range(highest_id):
    if i not in seat_ids and i-1 in seat_ids and i+1 in seat_ids:
        missing = i

print(highest_id)
print(missing)