"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint

arr = [randint(1, 100) for _ in range(10)]

min_i, max_i = 0, 0

for i, item in enumerate(arr):
	if arr[min_i] > item:
		min_i = i
	if arr[max_i] < item:
		max_i = i

print(f'Initial array: {arr}')
print(f'Min and max values indexes: {min_i, max_i}')

arr[min_i], arr[max_i] = arr[max_i], arr[min_i]

print(f'Swapped array: {arr}')
