# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # iterate both LL and add their digits, store carry in another digit, create new nodes with the reuslt and append to result LL
        result = ListNode(0)
        resultCur = result
        carry = 0
        while l1 or l2 or carry:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum // 10
            digit = sum % 10
            print(f'sum: {sum}, carry: {carry}, digit: {digit}')
            resultCur.next = ListNode(digit)
            resultCur = resultCur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result.next
