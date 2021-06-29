"""
4. Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

arr = [randint(1, 10) for _ in range(20)]

num_cnt = dict()

for i in arr:
	num_cnt[i] = (num_cnt.get(i) or 0) + 1

num_cnt = dict(sorted(num_cnt.items(), key=lambda item: -item[1]))

print(f'Initial array: {arr}')
print(f'Item count: {num_cnt}')
print(f'Most common item: {list(num_cnt.keys())[0]}')
