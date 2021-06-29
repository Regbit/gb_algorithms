"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

arr = [randint(-10, 10) for _ in range(10)]

min_i, max_i = 0, 0

for i, item in enumerate(arr):
	if arr[min_i] > item:
		min_i = i
	if arr[max_i] < item:
		max_i = i

start_i = 1 + (min_i if min_i < max_i else max_i)
end_i = min_i if min_i > max_i else max_i

slice_sum = 0

for i in arr[start_i: end_i]:
	slice_sum += i

print(f'Initial array: {arr}')
print(f'Min and max values indexes: {min_i, max_i}')
print(f'All values between min and max: {arr[start_i: end_i]}')
print(f'Sum of all values between min and max: {slice_sum}')
