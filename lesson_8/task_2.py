"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
"""


g = [
	[0, 0, 1, 1, 9, 0, 0, 0],
	[0, 0, 9, 4, 0, 0, 5, 0],
	[0, 9, 0, 0, 3, 0, 6, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 0],
	[0, 0, 0, 0, 0, 0, 5, 0],
	[0, 0, 7, 0, 8, 1, 0, 0],
	[0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
	length = len(graph)
	is_visited = [False] * length
	cost = [float('inf')] * length
	parent = [-1] * length

	cost[start] = 0
	min_cost = 0

	path = [[] for _ in range(length)]
	path[start].append(start)

	while min_cost < float('inf'):

		for i, walk_cost in enumerate(graph[start]):
			if walk_cost != 0 and not is_visited[i]:

				if cost[i] > walk_cost + cost[start]:
					cost[i] = walk_cost + cost[start]
					parent[i] = start

					path[i].clear()
					path[i].extend(path[start])
					path[i].append(i)

		min_cost = float('inf')
		for i in range(length):
			if min_cost > cost[i] and not is_visited[i]:
				min_cost = cost[i]
				start = i

		is_visited[start] = True

	return cost, path


walk_costs, paths = dijkstra(g, 0)

print(walk_costs)

for i, p in enumerate(paths):
	print(f'Путь до вершины {i}: {p if len(p) else "не существует"}')