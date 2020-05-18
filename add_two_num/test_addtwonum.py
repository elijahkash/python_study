import add_two_num


def test_1():
	lst1 = add_two_num.ListNode(3)
	lst1 = add_two_num.ListNode(4, lst1)
	lst1 = add_two_num.ListNode(2, lst1)

	lst2 = add_two_num.ListNode(4)
	lst2 = add_two_num.ListNode(6, lst2)
	lst2 = add_two_num.ListNode(5, lst2)

	assert add_two_num.Solution.addTwoNumbers(None, lst1, lst2).val == 807


def test_2():
	lst1 = add_two_num.ListNode(0)

	lst2 = add_two_num.ListNode(3)
	lst2 = add_two_num.ListNode(2, lst2)
	lst2 = add_two_num.ListNode(1, lst2)

	assert add_two_num.Solution.addTwoNumbers(None, lst1, lst2).val == 123


def test_3():
	lst1 = add_two_num.ListNode(1)
	lst1 = add_two_num.ListNode(8, lst1)

	lst2 = add_two_num.ListNode(0)

	assert add_two_num.Solution.addTwoNumbers(None, lst1, lst2).val == 81


def test_4():
	lst1 = add_two_num.ListNode(3)
	lst1 = add_two_num.ListNode(4, lst1)

	lst2 = add_two_num.ListNode(4)
	lst2 = add_two_num.ListNode(6, lst2)

	assert add_two_num.Solution.addTwoNumbers(None, lst1, lst2).val == 107

test_3()
