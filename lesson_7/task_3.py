"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random


def median(m):
	size = 2 * m + 1
	array = [random.randint(0, size) for _ in range(size)]
	random.shuffle(array)
	print(f'Initial array: {array}')

	num_cnt = dict()

	for i, item in enumerate(array):

		if item not in num_cnt:
			lt_cnt, eq_cnt, gt_cnt = 0, 0, 0
			for j, other_item in enumerate(array):
				if j == i:
					continue
				if other_item < item:
					lt_cnt += 1
				elif other_item > item:
					gt_cnt += 1
				else:
					eq_cnt += 1

			num_cnt[item] = lt_cnt, eq_cnt, gt_cnt

		if m - num_cnt[item][0] >= 0 and m - num_cnt[item][2] >= 0:
			return item


print(f'Median = {median(100)}')
