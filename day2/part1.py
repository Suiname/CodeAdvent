def gravity_assist(positions):
	for i in range(len(positions)):
		position = int(positions[i])
		if i % 4 == 0:
			if position == 99:
				return positions
			elif position == 1 or position == 2:
				result_index = int(positions[i+3])
				first_index = int(positions[i+1])
				second_index = int(positions[i+2])
				if position == 1:
					positions[result_index] = int(positions[first_index]) + int(positions[second_index])
				else:
					positions[result_index] = int(positions[first_index]) * int(positions[second_index])
	return positions


def make_array():
	result = []
	with open('input.txt') as lines:
		line = lines.readline()
		if line:
			result = line.split(',')
			line = lines.readline()
	return result


if __name__ == "__main__":
	test_list1 = [1,0,0,0,99]
	result_list1 = [2,0,0,0,99]
	test_result1 = gravity_assist(test_list1)
	print('test 1 passing: ', test_result1 == result_list1)
	test_list2 = [2,3,0,3,99]
	result_list2 = [2,3,0,6,99]
	test_result2 = gravity_assist(test_list2)
	print('test 2 passing: ', test_result2 == result_list2)
	test_list3 = [2,4,4,5,99,0]
	result_list3 = [2,4,4,5,99,9801]
	test_result3 = gravity_assist(test_list3)
	print('test 3 passing: ', test_result3 == result_list3)
	test_list4 = [1,1,1,4,99,5,6,0,99]
	result_list4 = [30,1,1,4,2,5,6,0,99]
	test_result4 = gravity_assist(test_list4)
	print('test 4 passing: ', test_result4 == result_list4)
	input_array = make_array()
	input_array[1] = 12
	input_array[2] = 2
	answer = gravity_assist(input_array)[0]
	print('answer: ', answer)
