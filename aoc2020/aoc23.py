def cup_solver(cups, iterations):
    i = 0
    max_cup = max(cups)
    save_old2 = cups[0]

    next_cup = {}
    for ind, cup in enumerate(cups):
        if ind == len(cups)-1:
            next_cup[cup] = cups[0]
            break
        else:
            next_cup[cup] = cups[ind+1] 
   
    while i < iterations:
        current_cup = save_old2
        destination = False
        pick_up = [next_cup[current_cup], next_cup[next_cup[current_cup]], next_cup[next_cup[next_cup[current_cup]]]]
        for cup in range(current_cup-1,0,-1):
            if cup not in pick_up:
                destination = cup
                break
        if not destination:
            for cup in [max_cup, max_cup - 1, max_cup - 2, max_cup - 3]:
                if cup not in pick_up:
                    destination = cup
                    break
        next_cup[current_cup] = next_cup[next_cup[next_cup[next_cup[current_cup]]]]
        save_old = next_cup[destination]
        save_old2 = next_cup[pick_up[2]]
        next_cup[destination] = pick_up[0]
        next_cup[pick_up[2]] = save_old
        i += 1

    cup = 1
    final_cups = [1]
    for i in range(len(cups)-1):
        cup = next_cup[cup]
        final_cups.append(cup)
    return final_cups, next_cup

cups = [1,3,5,4,6,8,7,2,9]
final_cups, next_cup = cup_solver(cups, 100)
final_cups = [str(cup) for cup in final_cups][1:]
final_cups = ''.join(final_cups)
print(final_cups)

for j in range(10,1000000+1):
    cups.append(j)
final_cups, next_cup = cup_solver(cups, 10000000)
print(next_cup[1]*next_cup[next_cup[1]])