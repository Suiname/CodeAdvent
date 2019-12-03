if __name__ == "__main__":
	total_fuel = 0
	with open('input.txt') as masses:
		line = masses.readline()
		while line:
			mass = line.strip()
			fuel = (int(mass) // 3) - 2
			while fuel > 0:
				total_fuel += fuel
				if fuel // 3 > 2:
					fuel = (fuel // 3) - 2
				else:
					fuel = 0
			line = masses.readline()
	print('answer:')
	print(total_fuel)