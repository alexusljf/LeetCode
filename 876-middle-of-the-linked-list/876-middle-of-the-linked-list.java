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
   	public ListNode middleNode(ListNode head) {
		// first get the size of the linked list
		int size = 1;
		int mid;
		ListNode cur = head;
		while(cur.next != null){
			cur = cur.next;
			size++;
		}
		if(size%2 == 0){
			mid = (size/2) + 1; // to get the second middle node
		}
		else{
			mid = (size+1)/2;
		}

		cur = head;
		// we iterate the LL again while decrementing mid
		// we stop when !(i>0), the last iteration was the node before the middle node, where we moved from mid-1 to mid-1.next which is mid
        int i = 1;
		while(i<mid){
			cur=cur.next;
			i++;
		}
		return cur;
	}
}