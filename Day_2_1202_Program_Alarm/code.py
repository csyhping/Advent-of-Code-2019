def run_program(add_1, add_2, ori_list):
	print('add1 = add2 = ', add_1, add_2)
	ori_list[1] = str(add_1)
	ori_list[2] = str(add_2)
	for i in range(0, len(ori_list) ,4):
		if ori_list[i] == '99':
			print(i, '99')
			break	
		elif ori_list[i] == '1':
			# print(i, '1')
			s1 = ori_list[int(ori_list[i + 1])]
			s2 = ori_list[int(ori_list[i + 2])]
			s = int(s1) + int(s2)
			ori_list[int(ori_list[i + 3])] = str(s)
			# print('s1 =, s2 = , sum = ', s1, s2, s)
			# print(ori_list)
		elif ori_list[i] == '2':
			# print(i, '2')
			s1 = ori_list[int(ori_list[i + 1])]
			s2 = ori_list[int(ori_list[i + 2])]
			s = int(s1) * int(s2)
			ori_list[int(ori_list[i + 3])] = str(s)
			# print('s1 =, s2 = , sum = ', s1, s2, s)
			# print(ori_list)
	return ori_list[0]

#------part 1------#
with open('input.txt', 'r') as f:
	order = f.read()
	orderlist = list(order.split(','))
	add_0 = run_program(12, 2, orderlist)
	print(add_0)

#------part 2------#

for i in range(100):
	for j in range(100):
		with open('input.txt', 'r') as f:
			order = f.read()
			orderlist = list(order.split(','))
			result = run_program(i, j, orderlist)
			if result == '19690720':
				print(i, j)
				exit(-1)
