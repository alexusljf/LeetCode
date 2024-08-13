# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        curl1 = l1
        curl2 = l2
        returnHead = ListNode(0,None)
        returnCur = returnHead
        carry=0
        while curl1 != None or curl2 != None:
            if curl1 == None:
                sum = curl2.val + carry
                if sum<10:
                    carry=0
                else:
                    sum-=10
                    carry=1
            elif curl2 == None:
                sum = curl1.val + carry
                if sum<10:
                    carry=0
                else:
                    sum-=10
                    carry=1
            else:
                sum = curl1.val + curl2.val + carry
                if sum < 10:
                    carry = 0
                else:
                    sum -= 10
                    carry = 1
            returnCur.next = ListNode(sum)
            if curl1 != None:
                curl1 = curl1.next
            if curl2 != None:
                curl2=curl2.next
            returnCur = returnCur.next
        if curl1 == None and curl2 == None and carry:
            returnCur.next=ListNode(carry)
        return returnHead.next
        
        