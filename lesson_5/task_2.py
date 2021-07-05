"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

hex_dict = {
	'0': 0,		'1': 1,		'2': 2,		'3': 3,
	'4': 4,		'5': 5,		'6': 6,		'7': 7,
	'8': 8,		'9': 9,		'A': 10,	'B': 11,
	'C': 12,	'D': 13,	'E': 14,	'F': 15
}

hex_dict_alt = dict((v, k) for k, v in hex_dict.items())


def to_dec(hex: deque) -> int:
	h = hex.copy()
	h.reverse()
	dec_val = 0

	for i, k in enumerate(h):
		dec_val += hex_dict[k] * 16**i

	return dec_val


def to_hex(dec: int) -> deque:
	hex = deque()
	to_div = dec
	while to_div != 0:
		to_div, rest = to_div // 16, to_div % 16
		hex.appendleft(hex_dict_alt[rest])

	return hex if len(hex) else deque(['0'])


def add(hex_1, hex_2):
	return to_hex(to_dec(hex_1) + to_dec(hex_2))


def mult(hex_1, hex_2):
	return to_hex(to_dec(hex_1) * to_dec(hex_2))


if __name__ == '__main__':
	a, b = (deque(hex.upper()) for hex in input("Введите два шестнадцатиричных числа через пробел:\n").split())

	for i in a:
		if i not in hex_dict.keys():
			raise ValueError

	for i in b:
		if i not in hex_dict.keys():
			raise ValueError

	print(f'{a} + {b} = {add(a, b)}')
	print(f'{a} * {b} = {mult(a, b)}')
