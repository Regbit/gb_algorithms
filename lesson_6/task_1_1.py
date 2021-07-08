import sys

print(sys.version, sys.platform)


def show_size(x, level=0):

	out = {
		x: {
			'type': x.__class__,
			'size': sys.getsizeof(x)
		}
	}

	if hasattr(x, '__iter__'):
		if hasattr(x, 'items'):
			for xx in x.items():
				out[x]['children'] = show_size(xx, level + 1)
		elif not isinstance(x, str):
			for xx in x:
				out[x]['children'] = show_size(xx, level + 1)

	return out


sizes = []


def func(n):
	sum, i = 0, 0
	if n > 0:
		while i < n:
			sum += ((-1) ** i) / 2 ** i
			i += 1

			state = {'func': globals()['func'], **{k: v for k, v in locals().items() if k in ['n', 'i', 'sum']}}
			iter = []
			for k, v in state.items():
				iter.append(show_size(v))
			sizes.append(iter)

	return sum


func(100)

mem = []

for i in sizes:
	mem_sum = 0
	for j in i:
		for k, v in j.items():
			mem_sum += v['size']

	mem.append(mem_sum)

print(f'max = {max(mem)}, min = {min(mem)}, avg = {round(sum(mem) / len(mem))}')

# 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)] win32
# max = 216, min = 216, avg = 216
