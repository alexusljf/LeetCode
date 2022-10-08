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
        int i = 1, size = 1;
        int mid;
        ListNode cur = head;
        // get the size of the LL
        while(cur.next != null){
            cur = cur.next;
            size++;
        }
        if(size==1){
            head=null;
            return head;
        }
        else{
        // get the mid point (2nd middle for even sizes)
        if(size%2 == 0){
            mid = (size/2) + 1;
        }
        else{
            mid = (size+1)/2;
        }
        cur = head;
        // while loop to stop at the node before mid
        while(i<mid-1){
            cur=cur.next;
            i++;
        }
	        ListNode midNode = cur.next;
	        cur.next=midNode.next;
	        return head;
    }
}
}