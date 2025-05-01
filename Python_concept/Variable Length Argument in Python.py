def sum_all(*args):
	result = 0
	for num in args:
		result += num
	return result

print(sum_all(1, 2, 3, 4, 5))
