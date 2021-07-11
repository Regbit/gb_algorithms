"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import random

size = 30
array = [random.randint(0, 49) for _ in range(size)]
random.shuffle(array)
print(f'Initial array: {array}')


def merge_sort(arr):
	if len(arr) == 1 or len(arr) == 0:
		return

	arr_left, arr_right = arr[:len(arr) // 2], arr[len(arr) // 2:]
	merge_sort(arr_left)
	merge_sort(arr_right)
	n = m = k = 0
	sorted_arr = [0] * len(arr)

	while n < len(arr_left) and m < len(arr_right):

		if arr_left[n] <= arr_right[m]:
			sorted_arr[k] = arr_left[n]
			n += 1
		else:
			sorted_arr[k] = arr_right[m]
			m += 1
		k += 1

	while n < len(arr_left):
		sorted_arr[k] = arr_left[n]
		n += 1
		k += 1

	while m < len(arr_right):
		sorted_arr[k] = arr_right[m]
		m += 1
		k += 1

	for i in range(len(arr)):
		arr[i] = sorted_arr[i]


merge_sort(array)
print(f'Sorted array: {array}')
