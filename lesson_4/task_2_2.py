import cProfile


def prime(nth):

	def _prime(n):

		def is_prime(n):
			d = 2
			while d * d <= n and n % d != 0:
				d += 1
			return d * d > n

		return [i for i in range(2, n) if is_prime(i)]

	span = 0
	step = nth * 2

	final_prime = []

	while len(final_prime) < nth:
		span += step
		final_prime = _prime(span)

	return final_prime[nth-1]


# print(prime(1000))

# cProfile.run('prime(1000)')


# timeit
# (base) D:\Workspace\Python\gb_algorithms\lesson_4>python -m timeit -n 100 -s "import task_2_2" "task_2_2.prime(1000)"
# 100 loops, best of 5: 29.2 msec per loop


# cProfile
# C:\Users\regbi\anaconda3\python.exe D:/Workspace/Python/gb_algorithms/lesson_4/task_2_2.py
#          20009 function calls in 0.032 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.032    0.032 <string>:1(<module>)
#         4    0.004    0.001    0.032    0.008 task_2_2.py:14(<listcomp>)
#         1    0.000    0.000    0.032    0.032 task_2_2.py:4(prime)
#         4    0.000    0.000    0.032    0.008 task_2_2.py:6(_prime)
#     19992    0.028    0.000    0.028    0.000 task_2_2.py:8(is_prime)
#         1    0.000    0.000    0.032    0.032 {built-in method builtins.exec}
#         5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
