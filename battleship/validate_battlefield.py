#!/usr/bin/env python3

import copy
from collections import namedtuple

Point = namedtuple('Point', 'x y')


def validate_battlefield(field):
	ships = split_ships(field)
	return True


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
				if i >= 0 and j >= 0 and work_field[i][j]:
					res.append(Point(i, j))
					work_field[i][j] = 0
	return res
