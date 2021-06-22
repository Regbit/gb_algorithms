"""
8. Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого).
"""
a, b, c = map(lambda x: float(x), input("Введите три числа через пробел:\n").split())
if a > b:
	if a < c:
		median = a
	elif b > c:
		median = b
	else:
		median = c
else:
	if a > c:
		median = a
	elif b > c:
		median = c
	else:
		median = b

print(f"Среднее = {median}")
