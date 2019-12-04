#------part 1------#
result1 = 0
with open('input.txt', 'r') as f:
	for line in f.readlines():
		data = int(line.strip())
		fuel = int(data/3)
		fuel -= 2
		result1 += fuel
print(result1)

#------part 2------#

result2 = 0
with open('input.txt', 'r') as f:
	for line in f.readlines():
		data = int(line.strip())
		fuel = int(data/3)
		fuel -= 2
		result2 += fuel
		while (int(fuel/3) - 2) >= 0:
			subfuel = int(fuel /3) - 2
			result2 += subfuel
			fuel = subfuel
			print(subfuel)
print(result2)