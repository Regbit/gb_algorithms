"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""
import cProfile


def test_func(f):
	series = [1, -0.5, 0.25, -0.125]
	s_sum = [sum(series[:i]) for i in range(len(series) + 1)]

	for i, el in enumerate(s_sum):
		assert f(i) == s_sum[i]
		print(f'Test {i} OK!')


def func(n):
	sum, i = 0, 0
	if n > 0:
		while i < n:
			sum += ((-1) ** i) / 2 ** i
			i += 1

	return sum


def main(n=None):
	el_nm = n if n else int(input("Введите количество элементов:\n"))
	return func(el_nm)


# test_func(func)

cProfile.run('main(100)')


# timeit
# (base) D:\Workspace\Python\gb_algorithms\lesson_4>python -m timeit -n 100 -s "import task_1_1" "task_1_1.main(100)"
# 100 loops, best of 5: 63 usec per loop


# cProfile
# C:\Users\regbi\anaconda3\python.exe D:/Workspace/Python/gb_algorithms/lesson_4/task_1_1.py
#          5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1_1.py:17(func)
#         1    0.000    0.000    0.000    0.000 task_1_1.py:27(main)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
