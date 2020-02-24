#!/usr/bin/env python3

import copy
from collections import namedtuple
from collections import Counter

Point = namedtuple('Point', 'x y')


def validate_battlefield(field):
	ships = split_ships(field)
	count_ships = Counter([len(ship) for ship in ships])
	return (
		len(count_ships) == 4
		and count_ships[1] == 4
		and count_ships[2] == 3
		and count_ships[3] == 2
		and count_ships[4] == 1
		and all((
			(
				all((dot.x == ship[0].x for dot in ship))
				or all((dot.y == ship[0].y for dot in ship))
			) for ship in ships))
	)


def split_ships(field):
	work_field = copy.deepcopy(field)
	res = []
	for i, x in enumerate(work_field):
		for j, y in enumerate(x):
			if y:
				res.append(get_ship(work_field, i, j))
	return res


def get_ship(work_field, src_i, src_j):
	res = []
	res.append(Point(src_i, src_j))
	work_field[src_i][src_j] = 0
	for dot in res:
		for i in range(dot.x - 1, dot.x + 2):
			for j in range(dot.y - 1, dot.y + 2):
				if 0 <= i < 10 and 0 <= j < 10 and work_field[i][j]:
					res.append(Point(i, j))
					work_field[i][j] = 0
	return res
