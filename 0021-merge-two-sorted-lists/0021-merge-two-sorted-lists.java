/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
		// base cases
		if (list1 == null && list2 == null) {
			return null;
		}
		if (list1 == null) {
			return list2;
		}
		if (list2 == null) {
			return list1;
		}
		ListNode returnHead = new ListNode();
		ListNode cur = new ListNode();
		// choose the 1st node
		if (list1.val < list2.val) {
			returnHead = list1;
			list1 = list1.next;
		} else {
			returnHead = list2;
			list2 = list2.next;
		}
		cur = returnHead;
		// while both lists not empty, compare each val and add to the returnHead
		while (list1 != null && list2 != null) {
			if (list1.val == list2.val) {
				cur.next = new ListNode(list1.val);
				cur.next.next = new ListNode(list1.val);
				cur = cur.next.next;
				list1 = list1.next;
				list2 = list2.next;
			} else if (list1.val < list2.val) {
				cur.next = new ListNode(list1.val);
				cur = cur.next;
				list1 = list1.next;
			} else if (list1.val > list2.val) {
				cur.next = new ListNode(list2.val);
				cur = cur.next;
				list2 = list2.next;
			}
		}
		if (list1 == null) {
			while (list2 != null) {
				cur.next = list2;
				list2 = list2.next;
				cur = cur.next;
			}
		}
		if (list2 == null) {
			while (list1 != null) {
				cur.next = list1;
				list1 = list1.next;
				cur = cur.next;
			}
		}
		return returnHead;
	}
}