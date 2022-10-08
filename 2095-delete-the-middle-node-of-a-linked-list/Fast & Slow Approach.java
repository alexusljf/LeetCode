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
    public ListNode deleteMiddle(ListNode head) {
       		// Fast and Slow Apporach (2 Pointers)
		// Fast pointer increments by 2 while Slow increments by 1. Once Fast.next == NULL (aka once Fast reaches the end of the LL),
		// Slow would have reached the middle of the LL
		if(head==null) 
			return head;
		if(head.next==null) 
			return head=null;
		ListNode fast = head;
		ListNode slow = head;
		ListNode cur = null;

		// Check for fast != null because if fast == null, fast.next will produce an error
		while(fast != null && fast.next != null) {
			cur=slow;
			slow=slow.next;
			fast=fast.next.next;
		}
		cur.next=slow.next;
		return head;

}
}