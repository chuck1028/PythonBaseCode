def square1(x):
    sum_so_far = 0
    for counter in range(x):
        sum_so_far = sum_so_far + x
	return sum_so_far

def square2(x):
    sum_so_far = 0
    for counter in range(x):
        sum_so_far = sum_so_far + x
    return sum_so_far
print(square1(10))
print(square2(10))
