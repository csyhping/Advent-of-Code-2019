import numpy as np 

#------part 1------#
def check_num(n1, n2, length):
	print(n1, n2, length)
	valid, count = 0, 0
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
		if valid == length - 1:
			for i in range(length - 1):
				if str_num[i] == str_num[i + 1]:
					count += 1
					valid = 0
					break
			valid = 0
	return count

result = check_num(193651, 649729, 6)
print(result)
