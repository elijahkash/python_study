from collections import deque
from collections import namedtuple


def spiralize(size):
	if not size:
		return [[]]
	Dot = namedtuple('Dot', 'x y')
	moves = deque((
		Dot(0, 1),
		Dot(1, 0),
		Dot(0, -1),
		Dot(-1, 0)
	))

	spiral = [[0] * size for _ in range(size)]
	spiral[0] = [1] * size
	if size != 2:
		spiral[size - 1] = [1] * size
	if size < 3:
		return spiral
	for i in range(size):
		spiral[0][i] = 1
		spiral[size - 1][i] = 1
		spiral[i][size - 1] = 1
	for i in range(2, size):
		spiral[i][0] = 1
	if size == 3:
		return spiral
	pos = Dot(2, 0)
	mv = 0
	while True:
		if spiral[pos.x + moves[0].x * 2][pos.y + moves[0].y * 2]:
			moves.rotate(-1)
			if mv == 1:
				break
			mv = 0
		pos = Dot(pos.x + moves[0].x, pos.y + moves[0].y)
		if spiral[pos.x + moves[0].x][pos.y + moves[0].y]:
			break
		mv += 1
		spiral[pos.x][pos.y] = 1
	return spiral

