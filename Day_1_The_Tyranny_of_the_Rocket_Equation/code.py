# part 1
result = 0
with open('input.txt', 'r') as f:
	for line in f.readlines():
		data = int(line.strip())
		fuel = int(data/3)
		fuel -= 2
		result += fuel
print(result)