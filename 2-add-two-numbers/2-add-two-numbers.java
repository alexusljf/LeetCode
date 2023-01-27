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
        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		ListNode returnNode = new ListNode();
		ListNode pointerNode = returnNode;
		int carry = 0; // carry variable to store the Tens digit (eg 4+7 = 11, 1 will be stored then the 1 in the Tens will be carried)
        while(l1 != null || l2 != null || carry != 0){ // 3 possible variables to be added
			int result = 0; // sum each node pair individually
			// check the 2 nodes first
			if(l1 != null){
				result += l1.val;
				l1 = l1.next;
			}
			if(l2 != null){
				result += l2.val;
				l2 = l2.next;
			}
			
			result += carry; // if there is a carry value
			carry = result / 10; // get new carry
			ListNode tempNode = new ListNode(); // create new ListNode to add to LL
			tempNode.val = result % 10; // store the Ones place digit
			pointerNode.next = tempNode; // traverse the LL
			pointerNode = pointerNode.next;
		}
		return returnNode.next; // return .next as the LL starts from the 2nd node
	}
}