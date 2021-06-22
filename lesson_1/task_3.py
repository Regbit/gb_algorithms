"""
3. Написать программу, которая генерирует в указанных пользователем границах:
	a. случайное целое число,
	b. случайное вещественное число,
	c. случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

from random import random, randint

a, b = input(f'Введите два элемента через пробел.\nПринимаются пары целых чисел, вещественных чисел и символов латинского алфавита от a до z:\n').split()
# out = ''

try:
	out = randint(min(int(a), int(b)), max(int(a), int(b)))
except Exception as e:
	try:
		out = min(float(a), float(b)) + random() * abs(float(a) - float(b))
	except Exception as e:
		try:
			if 'a' <= a <= 'z' and 'a' <= b <= 'z':
				out = chr(randint(min(ord(a), ord(b)), max(ord(a), ord(b))))
			else:
				raise
		except Exception as e:
			out = 'Неверный ввод'

print(f"Random: {out}")
