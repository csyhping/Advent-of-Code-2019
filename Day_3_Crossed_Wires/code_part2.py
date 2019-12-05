import numpy as np 
#------part 1------#
wires = np.loadtxt('input.txt', dtype = str)
wire1 = wires[0].split(',')
wire2 = wires[1].split(',')

w, wmax, wmin, h, hmax, hmin = 0, 0, 0, 0, 0, 0
for order in wire1:
	if order[0] == 'R':
		# print('R-', order)
		w += int(order[1:])
		wmax = max(w, wmax)
		# print('w = ', w, ' wmax = ', wmax)
	elif order[0] == 'L':
		# print('L-', order)
		w -= int(order[1:])
		wmin = min(w, wmin)
		# print('w = ', w, ' wmin = ', wmin)
	elif order[0] == 'U':
		# print('U-', order)
		h += int(order[1:])
		hmax = max(h, hmax)
		# print('h = ', h, ' hmax = ', hmax)
	elif order[0] == 'D':
		# print('D-', order)
		h-= int(order[1:])
		hmin = min(h, hmin)
		# print('h = ', h, ' hmax = ', hmin)
print(w, wmax, wmin, h, hmax, hmin)
w, h = 0, 0
for order in wire2:
	if order[0] == 'R':
		# print('R-', order)
		w += int(order[1:])
		wmax = max(w, wmax)
		# print('w = ', w, ' wmax = ', wmax)
	elif order[0] == 'L':
		# print('L-', order)
		w -= int(order[1:])
		wmin = min(w, wmin)
		# print('w = ', w, ' wmin = ', wmin)
	elif order[0] == 'U':
		# print('U-', order)
		h += int(order[1:])
		hmax = max(h, hmax)
		# print('h = ', h, ' hmax = ', hmax)
	elif order[0] == 'D':
		# print('D-', order)
		h-= int(order[1:])
		hmin = min(h, hmin)
		# print('h = ', h, ' hmax = ', hmin)
print(w, wmax, wmin, h, hmax, hmin)
col = wmax - wmin + 1 
row = hmax - hmin + 1 
print(row, col)
c_row = max(hmax, 0)
if wmin < 0:
	c_col = -wmin
else:
	c_col = 0
print('center = ', c_row, c_col)
center_r, center_c = c_row, c_col
space = np.zeros((row, col), dtype = int)
print(space.shape)
space[c_row][c_col] = -1
for order in wire1:
	# print(order, c_row, c_col)
	if order[0] == 'R':
		to_col = c_col + int(order[1:])
		# print('c_col =', c_col, ' to_col = ', to_col)
		space[c_row, c_col + 1: to_col + 1] = 1
		c_col = to_col
	elif order[0] == 'L':
		to_col = c_col - int(order[1:])
		# print('c_col =', c_col, ' to_col = ', to_col)
		space[c_row, to_col: c_col] = 1
		c_col = to_col
	elif order[0] == 'U':
		to_row = c_row - int(order[1:])
		# print('c_row =', c_row, ' to_row = ', to_row)
		space[to_row: c_row, c_col] = 1
		c_row = to_row
	elif order[0] == 'D':
		to_row = c_row + int(order[1:])
		# print('c_row =', c_row, ' to_row = ', to_row)
		space[c_row + 1: to_row + 1, c_col] = 1
		c_row = to_row
c_row, c_col = center_r, center_c
print(c_row, c_col)
for order in wire2:
	# print(order, c_row, c_col)
	if order[0] == 'R':
		to_col = c_col + int(order[1:])
		# print('c_col =', c_col, ' to_col = ', to_col)
		tmp = space[c_row, c_col + 1: to_col + 1]
		tmp[tmp == 1] = 2
		space[c_row, c_col + 1: to_col + 1] = tmp
		c_col = to_col
	elif order[0] == 'L':
		to_col = c_col - int(order[1:])
		# print('c_col =', c_col, ' to_col = ', to_col)
		tmp = space[c_row, to_col: c_col]
		tmp[tmp == 1] = 2
		space[c_row, to_col: c_col] = tmp
		c_col = to_col
	elif order[0] == 'U':
		to_row = c_row - int(order[1:])
		# print('c_row =', c_row, ' to_row = ', to_row)
		tmp = space[to_row: c_row, c_col]
		tmp[tmp == 1] = 2
		space[to_row: c_row, c_col] = tmp
		c_row = to_row
	elif order[0] == 'D':
		to_row = c_row + int(order[1:])
		# print('c_row =', c_row, ' to_row = ', to_row)
		tmp = space[c_row + 1: to_row + 1, c_col]
		tmp[tmp == 1] = 2
		space[c_row + 1: to_row + 1, c_col] = tmp
		c_row = to_row
num_intersection = np.sum(space == 2)
p = np.where(space == 2)
print(num_intersection)
print(p)
d_intersection = {}
c_row, c_col = center_r, center_c
steps = 0
for order in wire1:
	print(order, c_row, c_col, steps)
	if order[0] == 'R':
		to_col = c_col + int(order[1:])
		# print('c_col =', c_col, ' to_col = ', to_col)
		tmp = space[c_row, c_col + 1: to_col + 1]
		# check if there is intersection
		if 2 in tmp:
			pos = np.where(tmp == 2)
			# print(pos)
			for k in range(len(pos[0])):
				act_row = 0 + c_row
				act_col = pos[0][k] + c_col + 1
				if (act_row, act_col) in d_intersection:
					continue
				else:
					d_intersection[act_row, act_col] = steps + pos[0][k] + 1
		steps += int(order[1:])
		c_col = to_col
	elif order[0] == 'L':
		to_col = c_col - int(order[1:])
		# print('c_col =', c_col, ' to_col = ', to_col)
		tmp = space[c_row, to_col: c_col]
		# check if there is intersection
		if 2 in tmp:
			pos = np.where(tmp == 2)
			# print(pos)
			for k in range(len(pos[0])):
				act_row = 0 + c_row
				act_col = pos[0][k] + to_col
				if (act_row, act_col) in d_intersection:
					continue
				else:
					d_intersection[act_row, act_col] = steps + int(order[1:]) - pos[0][k]
		steps += int(order[1:])
		c_col = to_col
	elif order[0] == 'U':
		to_row = c_row - int(order[1:])
		# print('c_row =', c_row, ' to_row = ', to_row)
		tmp = space[to_row: c_row, c_col]
		# print(tmp)
		# check if there is intersection
		if 2 in tmp:
			pos = np.where(tmp == 2)
			for k in range(len(pos[0])):				
				act_row = pos[0][k] +to_row
				act_col = 0 + c_col
				if (act_row, act_col) in d_intersection:
					continue
				else:
					d_intersection[act_row, act_col] = steps + int(order[1:]) - pos[0][k]
		steps += int(order[1:])
		c_row = to_row
	elif order[0] == 'D':
		to_row = c_row + int(order[1:])
		# print('c_row =', c_row, ' to_row = ', to_row)
		tmp = space[c_row + 1: to_row + 1, c_col]
		# check if there is intersection
		if 2 in tmp:
			pos = np.where(tmp == 2)
			# print(pos)
			for k in range(len(pos[0])):
				act_row = pos[0][k] +c_row + 1
				act_col = 0 + c_col
				if (act_row, act_col) in d_intersection:
					continue
				else:
					d_intersection[act_row, act_col] = steps + pos[0][k] + 1
		steps += int(order[1:])
		c_row = to_row

print(d_intersection)
count_d = {}
c_row, c_col = center_r, center_c
steps = 0
for order in wire2:
	if order[0] == 'R':
		to_col = c_col + int(order[1:])
		# print('c_col =', c_col, ' to_col = ', to_col)
		tmp = space[c_row, c_col + 1: to_col + 1]
		# check if there is intersection
		if 2 in tmp:
			pos = np.where(tmp == 2)
			for k in range(len(pos[0])):
				act_row = 0 + c_row
				act_col = pos[0][k] + c_col + 1
				if (act_row, act_col) in count_d:
					continue
				else:
					d_intersection[act_row, act_col] += steps + pos[0][k] + 1
					count_d[act_row, act_col] = 1
		steps += int(order[1:])
		c_col = to_col
	elif order[0] == 'L':
		to_col = c_col - int(order[1:])
		# print('c_col =', c_col, ' to_col = ', to_col)
		tmp = space[c_row, to_col: c_col]
		# check if there is intersection
		if 2 in tmp:
			pos = np.where(tmp == 2)
			# print(pos)
			for k in range(len(pos[0])):
				act_row = 0 + c_row
				act_col = pos[0][k] + to_col
				if (act_row, act_col) in count_d:
					continue
				else:
					d_intersection[act_row, act_col] += steps + int(order[1:]) - pos[0][k]
					count_d[act_row, act_col] = 1
		steps += int(order[1:])
		c_col = to_col
	elif order[0] == 'U':
		to_row = c_row - int(order[1:])
		# print('c_row =', c_row, ' to_row = ', to_row)
		tmp = space[to_row: c_row, c_col]
		# print(tmp)
		# check if there is intersection
		if 2 in tmp:
			# print('x')
			pos = np.where(tmp == 2)
			# print(pos[0])
			for k in range(len(pos[0])):				
				act_row = pos[0][k] +to_row
				act_col = 0 + c_col
				if (act_row, act_col) in count_d:
					continue
				else:
					d_intersection[act_row, act_col] += steps + int(order[1:]) - pos[0][k]
					count_d[act_row, act_col] = 1
		steps += int(order[1:])
		c_row = to_row
	elif order[0] == 'D':
		to_row = c_row + int(order[1:])
		# print('c_row =', c_row, ' to_row = ', to_row)
		tmp = space[c_row + 1: to_row + 1, c_col]
		# check if there is intersection
		if 2 in tmp:
			pos = np.where(tmp == 2)
			# print(pos)
			for k in range(len(pos[0])):
				act_row = pos[0][k] +c_row + 1
				act_col = 0 + c_col
				if (act_row, act_col) in count_d:
					continue
				else:
					d_intersection[act_row, act_col] += steps + pos[0][k] + 1
					count_d[act_row, act_col] = 1
		steps += int(order[1:])
		c_row = to_row
print(d_intersection)
print(min(d_intersection.values()))