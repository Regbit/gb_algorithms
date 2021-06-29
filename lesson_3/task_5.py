"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""

from random import randint

arr = [randint(-100, 100) for _ in range(30)]

target_i = -1

for i, item in enumerate(arr):
	if target_i == -1:
		if item < 0:
			target_i = i
		else:
			continue
	elif arr[target_i] < item < 0:
		target_i = i


print(f'Initial array: {arr}')
print(f'Max negative is "{arr[target_i]}" at position = {target_i}')
