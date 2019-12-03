from part1 import gravity_assist, make_array


def find_params():
	for i in range(100):
		for j in range(100):
			array = make_array()
			array[1] = i
			array[2] = j
			result = gravity_assist(array)
			if result[0] == 19690720:
				return array
	return None

if __name__ == "__main__":
	params = find_params()
	noun = params[1]
	verb = params[2]
	print('noun:', noun)
	print('verb:', verb)
	print('100 * noun + verb:', 100 * noun + verb)