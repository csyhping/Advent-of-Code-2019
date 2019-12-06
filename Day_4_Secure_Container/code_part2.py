import numpy as np 

#------part 2------#
def check_num(n1, n2, length):
	print(n1, n2, length)
	valid, count= 0, 0
	for num in range(n1, n2 + 1):
		str_num = str(num)
		# check increase
		for i in range(length - 1):
			if str_num[i] <= str_num[i + 1]:
				valid += 1
			else:
				valid = 0
				break

		# check double
		dict_count = {}
		d_count = 1
		# flag = 0
		if valid == length - 1:
			for i in range(length - 1):
				if str_num[i] == str_num[i + 1]:
					d_count += 1
					if i == length - 1 - 1:
						dict_count[str_num[i]] = d_count

				else:
					if d_count >= 2:
						# has found a group of same digits
						dict_count[str_num[i]] = d_count
						d_count = 1
			valid = 0
		if 2 in dict_count.values():
				count += 1
				print(num)
				# print(dict_count)	
		# if len(dict_count.keys()) != 0:
		# 	for value in dict_count.values():
		# 		if value % 2 != 0:
		# 			flag = 1
		# 			break
		# 	if flag == 0:
		# 		count += 1
		# 		print(num)
		# 		# print(dict_count)	

	return count

result = check_num(193651, 649729, 6)
print(result)
