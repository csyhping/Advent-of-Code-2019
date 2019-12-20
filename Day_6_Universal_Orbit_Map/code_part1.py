import numpy as np 
from tqdm import tqdm as tqdm 
def countOrbits(all_orbits, curr_planet, curr_count):
	# print('checking ===', curr_planet)
	# count orbits for each planet
	for orbit in all_orbits:
		orbb = orbit.split(')')
		p1, p2 = orbb[0], orbb[1]
		# print(orbb)
		if p2 == curr_planet:
			if p1 != 'COM':
				curr_count += 1
				subcount = countOrbits(all_orbits, p1, 0)
				return subcount + curr_count
			else:
				curr_count += 1
	# counts = 0
	return curr_count

orbits = np.loadtxt('input.txt', dtype = str)
planets = []

# get all planets 
for orbit in orbits:
	orbb = orbit.split(')')
	planets.append(orbb[0])
	planets.append(orbb[1])

# remove duplicate planets
planets = set(planets)

# delete COM
planets.remove('COM')
print(planets)
orbitcount = 0
# count indirect and direct orbits for each planet
for planet in tqdm(planets):
	# print('current plane = ', planet)
	sub_count = countOrbits(orbits, planet, 0)
	# print(sub_count)
	orbitcount += sub_count

print(orbitcount)