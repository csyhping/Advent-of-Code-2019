import numpy as np 

def countOrbits(all_orbits, curr_planet, curr_count):
	# count orbits for each planet
	for orbit in all_orbits:
		orbb = orbit.split(')')
		p1, p2 = orbb[0], orbb[1]
		print(orbb)
		if p2 == curr_planet:
			if p1 != 'A':
				curr_count += 1
				subcount = countOrbits(all_orbits, p1, 0)
				return subcount
			else:
				curr_count += 1
	# counts = 0
	return curr_count

orbits = np.loadtxt('case.txt', dtype = str)
planets = []

# get all planets 
for orbit in orbits:
	orbb = orbit.split(')')
	planets.append(orbb[0])
	planets.append(orbb[1])

# remove duplicate planets
planets = set(planets)

# delete COM
planets.remove('A')

orbitcount = 0
# count indirect and direct orbits for each planet
for planet in planets:
	sub_count = countOrbits(orbits, planet, 0)
	orbitcount += sub_count