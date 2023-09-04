/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
	public boolean hasCycle(ListNode head) {
		ListNode slow = head;
		ListNode fast = head;
		while (fast != null) {
            // if reach end of LL, break
			if (fast.next == null || fast.next.next == null) {
				break;
			}
			fast = fast.next.next;
			slow = slow.next;
			if (fast == slow) {
				return true;
			}
		}
		return false;
	}
}