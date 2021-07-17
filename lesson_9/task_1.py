"""
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.

Примечания:
	* в сумму не включаем пустую строку и строку целиком;
	* без использования функций для вычисления хэша
	(hash(), sha1() или любой другой из модуля hashlib)
	задача считается не решённой.
"""

import hashlib
from typing import Dict
from collections import defaultdict


def rabin_karp_cnt(s: str, subs: str) -> int:
	assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустыми'
	assert len(s) >= len(subs), 'Подстрока длинее стркои'

	cnt = 0

	len_sub = len(subs)
	h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

	for i in range(len(s) - len_sub + 1):
		if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
			cnt += 1

	return cnt


def count_all_subs(s: str, verbose=False) -> Dict[str, int]:

	clean_s = s.strip()

	assert clean_s, 'Строка не может быть пустой'

	out = defaultdict(int)
	i = 0

	for sub_len in range(1, len(clean_s)):
		for sub_start in range(len(s) - sub_len + 1):
			sub = clean_s[sub_start:sub_start+sub_len]
			if sub.strip() and sub not in out.keys():
				out[sub] = rabin_karp_cnt(s, sub)
				if verbose:
					print(f'[{i}] "{sub}": {out[sub]}')
					i += 1

	return out


s = input('Введите строку: ')
print(f'Количество различных подстрок: {len(count_all_subs(s, True).keys())}')
