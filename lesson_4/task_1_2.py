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
		print(f'Test {i} OK! {f(i)} == {s_sum[i]}')


def func(n):

	def elem_by_index(i):
		return ((-1) ** i) / 2 ** i

	if n == 0:
		return 0
	else:
		return func(n - 1) + elem_by_index(n - 1)


def main(n=None):
	el_nm = n if n else int(input("Введите количество элементов:\n"))
	return func(el_nm)


# test_func(func)

cProfile.run('main(100)')


# timeit
# (base) D:\Workspace\Python\gb_algorithms\lesson_4>python -m timeit -n 100 -s "import task_1_2" "task_1_2.main(100)"
# 100 loops, best of 5: 86 usec per loop


# cProfile
# C:\Users\regbi\anaconda3\python.exe D:/Workspace/Python/gb_algorithms/lesson_4/task_1_2.py
#          205 function calls (105 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     101/1    0.000    0.000    0.000    0.000 task_1_2.py:17(func)
#       100    0.000    0.000    0.000    0.000 task_1_2.py:19(elem_by_index)
#         1    0.000    0.000    0.000    0.000 task_1_2.py:29(main)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
