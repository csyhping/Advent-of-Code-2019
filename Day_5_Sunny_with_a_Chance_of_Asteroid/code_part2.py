import numpy as np  

def unittest(inputs, instruction, program, pos):
	if instruction == 1:
		# sum
		# print('instruction mode = 1, sum')
		s1, s2, pm = program[program[pos + 1]], program[program[pos + 2]], program[pos + 3]
		ssum = s1 + s2
		program[pm] = ssum
		pos += 4
		# print(s1, s2, ssum)
	elif instruction == 2:
		# multi
		# print('instruction mode = 2, multi')
		m1, m2, pm = program[program[pos + 1]], program[program[pos + 2]], program[pos + 3]
		multi = m1 * m2
		program[pm] = multi
		pos += 4
		# print(m1, m2, multi)
	elif instruction == 3:
		# take input
		# print('instruction mode = 3, take input')
		pm = program[pos + 1]
		program[pm] = inputs
		pos += 2
	elif instruction == 4:
		# output
		# print('instruction mode = 4, output')
		pm = program[pos + 1]
		print('output = ', program[pm])
		pos += 2
	elif instruction == 5:
		# jump if true
		j1, j2= program[program[pos + 1]], program[program[pos + 2]]
		if j1 != 0:
			pos = j2
		else:
			pos += 2
	elif instruction == 6:
		# jump if false
		j1, j2= program[program[pos + 1]], program[program[pos + 2]]
		if j1 == 0:
			pos = j2
		else:
			pos += 2
	elif instruction == 7:
		# less than
		j1, j2, pm = program[program[pos + 1]], program[program[pos + 2]], program[program[pos + 3]]
		if j1 < j2:
			program[pm] = 1
		else:
			program[pm] = 0
		pos += 4
	elif instruction == 8:
		# equals
		j1, j2, pm = program[program[pos + 1]], program[program[pos + 2]], program[program[pos + 3]]
		if j1 == j2:
			program[pm] = 1
		else:
			program[pm] = 0
		pos += 4
	elif instruction == 99:
		# halt 
		# print('instruction mode = 99, HALT')
		exit(-1)
	else:
		# decode instructions
		# print('instruction mode = decode, decode = ', program[pos])
		ins = program[pos] % 100
		pm_code_1 = (int)(program[pos] / 100 ) % 10
		pm_code_2 = (int)(program[pos] / 1000 ) % 10
		pm_code_3 = (int)(program[pos] / 10000 ) % 10
		if ins == 1:
			# print('decoded ins mode = 1, sum')
			pm_1, pm_2, pm_3 = program[pos + 1], program[pos + 2], program[pos + 3]
			s1 = decode_pm(pm_code_1, program, pm_1)
			s2 = decode_pm(pm_code_2, program, pm_2)
			ssum = s1 + s2
			program[pm_3] = ssum
			pos += 4
		elif ins == 2:
			# print('decoded ins mode = 2, multi')
			pm_1, pm_2, pm_3 = program[pos + 1], program[pos + 2], program[pos + 3]
			s1 = decode_pm(pm_code_1, program, pm_1)
			s2 = decode_pm(pm_code_2, program, pm_2)
			multi = s1 * s2
			program[pm_3] = multi
			pos += 4
		elif ins == 3:
			# print('decoded ins mode = 3, take input')
			pm = program[pos + 1]
			program[pm] = inputs
			pos += 2
		elif ins == 4:
			# print('decoded ins mode = 4, output')
			pm = program[pos + 1]
			outputs = decode_pm(pm_code_1, program, pm)
			print('output = ', outputs)
			pos += 2
		elif ins == 5:
			pm_1, pm_2= program[program[pos + 1]], program[program[pos + 2]]
			j1 = decode_pm(pm_code_1, program, pm_1)
			j2 = decode_pm(pm_code_2, program, pm_2)
			if j1 != 0:
				pos = j2
			else:
				pos += 2
		elif ins == 6:
			pm_1, pm_2= program[program[pos + 1]], program[program[pos + 2]]
			j1 = decode_pm(pm_code_1, program, pm_1)
			j2 = decode_pm(pm_code_2, program, pm_2)
			if j1 == 0:
				pos = j2
			else:
				pos += 2
		elif ins == 7:
			pm_1, pm_2, pm = program[program[pos + 1]], program[program[pos + 2]], program[program[pos + 3]]
			
		elif ins == 8:
			pm_1, pm_2, pm = program[program[pos + 1]], program[program[pos + 2]], program[program[pos + 3]]
			


		elif ins == 99:
			# print('decoded ins mode = 99, HALT')
			exit(-1)
	return program, pos

# decode parameter code
def decode_pm(pmcode, program, para):
	if pmcode == 0:
		# pos mode
		return program[para]
	elif pmcode == 1:
		# immidiate mode
		return para

# load the input
programs = np.loadtxt('input.txt', delimiter = ',', dtype = int)
inputs = 1
# test input = 1, air conditioner unit
programs, i = unittest(inputs, programs[0], programs, 0)
# test others 
i = 0
while programs[i] != 99:
	# print('==> i = ', i)
	programs, i = unittest(inputs, programs[i], programs, i)
