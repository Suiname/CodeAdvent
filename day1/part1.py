if __name__ == "__main__":
	fuel = 0
	with open('input.txt') as masses:
		line = masses.readline()
		while line:
			mass = line.strip()
			fuel += (int(mass) // 3) - 2 
			line = masses.readline()
	print('answer:')
	print(fuel)