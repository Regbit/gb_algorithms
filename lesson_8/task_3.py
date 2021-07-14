"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).

Примечания:
	a. граф должен храниться в виде списка смежности;
	b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""


from random import random
from typing import List


def print_graph(graph):
	for r in graph:
		print(r)


def make_random_graph_matrix(n: int, p=0.5) -> List[List[int]]:
	"""
	Generates random graph with n vertexes
	:param n
	number of vertexes
	:param p
	connection probability
	"""
	g = None
	graph_made = False

	def link_decider(p) -> int:
		"""
		Used to change connection probability.
		:param p float
		"""
		return 1 if random() > (1 - p) else 0

	while not graph_made:
		g = [[link_decider(p) for _ in range(n)] for _ in range(n)]
		graph_made = True

		for i in range(n):
			g[i][i] = 0

			if sum(g[i]) == 0 and sum([r[i] for r in g]) == 0:
				graph_made = False

	return g


def graph_matrix_to_list(graph):
	l = len(graph)
	out_graph = [[] for _ in range(l)]

	for i in range(l):
		for j in range(l):
			if j == i:
				continue
			if graph[i][j]:
				out_graph[i].append(j)

	return out_graph


def dfs(graph, visited=None, start=0, level=0):

	if level == 0:
		print('Level | Tree')

	max_depth = level

	if not visited:
		visited = []
	visited.append(start)

	for i in graph[start]:
		if i not in visited:
			print(''.join([f'[{level+1:>3}] | ', ' ' * 4 * level, f'{start}->{i}']))
			res = dfs(graph, visited, i, level + 1)
			if max_depth < res[0]:
				max_depth = res[0]

	return max_depth, visited


g = make_random_graph_matrix(10, 0.25)
print_graph(g)
print('-'*25)
g_l = graph_matrix_to_list(g)
print(dfs(g_l))
