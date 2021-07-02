"""
2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""
import cProfile


def sieve(nth):

	def _sieve(n):
		sieve = [i for i in range(n)]
		sieve[1] = 0

		for i in range(2, n):
			if sieve[i] != 0:
				j = i * 2

				while j < n:
					sieve[j] = 0
					j += i

		return [i for i in sieve if i != 0]

	span = 0
	step = nth * 2

	final_sieve = []

	while len(final_sieve) < nth:
		span += step
		final_sieve = _sieve(span)

	return final_sieve[nth-1]


# print(sieve(100))


# cProfile.run('sieve(1000)')


# timeit
# (base) D:\Workspace\Python\gb_algorithms\lesson_4>python -m timeit -n 100 -s "import task_2_1" "task_2_1.sieve(1000)"
# 100 loops, best of 5: 6.87 msec per loop


# cProfile
# C:\Users\regbi\anaconda3\python.exe D:/Workspace/Python/gb_algorithms/lesson_4/task_2_1.py
#          21 function calls in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.000    0.000    0.007    0.007 task_2_1.py:14(sieve)
#         4    0.006    0.001    0.007    0.002 task_2_1.py:16(_sieve)
#         4    0.001    0.000    0.001    0.000 task_2_1.py:17(<listcomp>)
#         4    0.001    0.000    0.001    0.000 task_2_1.py:28(<listcomp>)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#         5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


