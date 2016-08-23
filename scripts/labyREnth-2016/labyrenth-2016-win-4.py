queue = [(0, 13, 7, -1, -1)]     # bootle 1 2 3, previous vertex, previous move
max_water = (19, 13, 7)
it = 0
moves = ((1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2))
already_checked = set()
while it < len(queue):
    cur_state = queue[it]
    already_checked.add(cur_state[:3])
    if cur_state[0] == 10 and cur_state[1] == 10:
        break
    for i in range(len(moves)):
        move = moves[i]
        water_sum = cur_state[move[0] - 1] + cur_state[move[1] - 1]
        new_state = list(cur_state)
        new_state[move[1] - 1] = min(water_sum, max_water[move[1] - 1])
        water_sum -= new_state[move[1] - 1]
        new_state[move[0] - 1] = water_sum
        new_state[3] = it
        new_state[4] = i
        new_state = tuple(new_state)
        if new_state[:3] not in already_checked:
            queue.append(new_state)
    it += 1

ans_it = it
ans = []
while ans_it >= 0:
    ans.append(moves[queue[ans_it][4]])
    ans_it = queue[ans_it][3]

ans = ans[:-1]
print(''.join(str(x[0]) + str(x[1]) for x in ans[::-1]))