"""
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""

from collections import defaultdict

companies_dict = defaultdict(list)

avg = lambda arr: sum(arr) / len(arr)

for i in range(int(input("Введите количество пердприятий:\n"))):
	name = input(f"\nВведите название предприятия №{i + 1}:\n")

	companies_dict[name].extend(
		map(
			lambda a: float(a),
			input(f"Введите доход за четыре квартала предприятия №{i + 1} через пробел:\n").split()
		)
	)
	print(f'Средний доход предприятия "{name}" = {avg(companies_dict[name])}')

total_avg = avg([avg(v) for v in list(companies_dict.values())])

print(f'Средний доход по всем предприятиям = {total_avg}')
print(f'Предприятия со средним доходом выше среднего дохода по всем = {[k for k, v in companies_dict.items() if avg(v) > total_avg]}')
