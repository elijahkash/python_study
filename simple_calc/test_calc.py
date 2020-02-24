import pytest

from simple_calc import calc

# use --tb=line


@pytest.mark.parametrize(
	"test_input,expected", [
		["1 + 1", 2],
		["8/16", 0.5],
		["3 -(-1)", 4],
		["2 + -2", 0],
		["10- 2- -5", 13],
		["(((10)))", 10],
		["3 * 5", 15],
		["-7 * -(6 / 3)", 14]
	]
)
def test_simple(test_input, expected):
	msg = f'{calc(test_input)} == {expected}\t\t{test_input}'
	assert calc(test_input) == expected, msg
