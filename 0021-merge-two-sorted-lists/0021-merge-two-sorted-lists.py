# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        cur = None
        count = 0
        while list1 != None or list2 != None:
            if count ==0:
                if list1 is None:
                    return list2
                if list2 is None:
                    return list1
                if list1.val < list2.val:   
                    head = list1
                    cur = list1
                    list1 = list1.next
                else:
                    head = list2
                    cur = list2
                    list2 = list2.next
                count+=1
            else:
                if list1 is None:
                    cur.next = list2
                    break
                if list2 is None:
                    cur.next = list1
                    break
                if list1.val < list2.val:
                    cur.next = list1
                    cur = cur.next
                    list1 = list1.next
                else:
                    cur.next = list2
                    cur = cur.next
                    list2 = list2.next
        return head
                
                
                