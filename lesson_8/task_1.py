"""
1. На улице встретились N друзей.
Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""


def print_graph(graph):
	for r in graph:
		print(r)


def handshakes(friends_cnt):

	graph = [[0 for _ in range(friends_cnt)] for _ in range(friends_cnt)]

	# Направленный граф
	for i, r in enumerate(graph):
		graph[i] = r[:i+1] + ([1] * (friends_cnt - i - 1))

	return graph, sum([sum(i) for i in graph])


g, n = handshakes(7)
print_graph(g)
print(f'Handshake count: {n}')
