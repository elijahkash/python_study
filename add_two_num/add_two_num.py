from typing import Any

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		num1: str = ''
		num2: str = ''

		while l1:
			num1 += str(l1.val)
			l1 = l1.next
		while l2:
			num2 += str(l2.val)
			l2 = l2.next
		# return ListNode(int(num1) + int(num2))
		res_List: Any = None
		res = str(int(num1) + int(num2))
		while res:
			res_List = ListNode(int(res[0]), res_List)
			res = res[1:]
		return res_List

# C
# struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
#     struct ListNode *res = NULL;
#     struct ListNode *tail = NULL;
#     struct ListNode *new;
#     int cur = 0;
#     while (l1 || l2 || cur)
#     {
#         if (l1)
#         {
#             cur += l1->val;
#             l1 = l1->next;
#         }
#         if (l2)
#         {
#             cur += l2->val;
#             l2 = l2->next;
#         }
#         new = malloc(sizeof(struct ListNode));
#         new->val = cur % 10;
#         new->next = NULL;
#         if (res)
#         {
#             tail->next = new;
#             tail = new;
#         }
#         else
#         {
#             res = new;
#             tail = new;
#         }
#         cur /= 10;
#     }
#     return (res);
# }
