"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""

from collections import defaultdict, deque


class Node:

	def __init__(self, data=None, weight=0, left=None, right=None):
		self.data = data
		self._weight = weight
		self.left = left
		self.right = right

	@property
	def weight(self):
		return sum([
			self.left.weight if self.left else 0,
			self.right.weight if self.right else 0,
			self._weight
		])

	@property
	def desc_simple(self):
		return f'{self.__class__.__name__}("{self.data or ""}", {self.weight})'

	def __repr__(self):
		left = f', l={self.left.desc_simple}' if self.left else ""
		right = f', r={self.right.desc_simple}' if self.right else ""
		return f'{self.desc_simple[:len(self.desc_simple) -1]}{left}{right})'


def search( tree, ch, path=''):
	res_path = None

	if tree.data == ch:
		res_path = path

	if not res_path and tree.left:
		res_path = search(tree=tree.left, ch=ch, path=f'{path}0')

	if not res_path and tree.right:
		res_path = search(tree=tree.right, ch=ch, path=f'{path}1')

	return res_path


def make_tree(ch_cnt, verbose=False) -> Node:
	node_que = deque()
	for ch in sorted(ch_cnt, key=lambda k: ch_cnt[k]):
		node_que.append(Node(data=ch, weight=ch_cnt[ch]))

	iteration = 0

	if verbose:
		print(f'\n{iteration}: {node_que}\n')

	while len(node_que) > 1:
		n_1, n_2 = node_que.popleft(), node_que.popleft()
		n = Node(left=n_1, right=n_2)

		if verbose:
			print(f'\tPopped:\n\t\t{n_1}\n\t\t{n_2}')
			print(f'\tNew node: {n}')
			print(f'\tRest of the que: {node_que}')

		if len(node_que):
			for i, n_from_que in enumerate(node_que):
				if n.weight <= n_from_que.weight:
					node_que.insert(i, n)
					if verbose:
						print(f"\tInserting at {i} (before {n_from_que})")
					break
				elif i == len(node_que) - 1:
					node_que.append(n)
					if verbose:
						print(f"\tInserting in the end")
					break

		else:
			node_que.append(n)

		iteration += 1

		if verbose:
			print(f'\n{iteration}: {node_que}\n')

	return node_que.pop()


def huffman_encode(s: str, verbose=False) -> str:
	assert s, 'Строка не может быть пустой'
	char_cnt = defaultdict(int)
	for ch in s:
		char_cnt[ch] += 1

	if verbose:
		print(char_cnt)

	tree = make_tree(char_cnt, verbose)
	encoded_ch = {ch: search(tree, ch) for ch in char_cnt.keys()}

	if verbose:
		sorted_res = {ch[0]: ch[1] for ch in sorted(
			encoded_ch.items(),
			key=lambda item: len(item[1]) ** 3 + int(item[1], 2)
		)}

		print('-' * 80, end='\n\n')
		print('Huffman table:\n')
		for k, v in sorted_res.items():
			print(f'"{k}": {v}')

		print()
		print('-' * 80, end='\n\n')

	encoded_s = []

	for ch in s:
		encoded_s.append(encoded_ch[ch])

	return ' '.join(encoded_s)


# init_str = 'Here\'s some text to encode! Does it work? Looks like it. What do you think?'
init_str = 'beep boop beer!'

res = huffman_encode(init_str, True)

print(f'Initial string:\n"{init_str}"\n')
print(f'Encoded string (with spacing between characters):\n{res}')
