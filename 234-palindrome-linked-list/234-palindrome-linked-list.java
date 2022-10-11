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

import java.util.Stack;

class Solution {
    public boolean isPalindrome(ListNode head) {
    	boolean isPalindrome = true;
    	int stackVal = 0;
    	Stack<Integer> stack = new Stack<Integer>();
    	// iterate through LL, pushing nodes value into a stack
    	// then iterate through LL again and pop nodes each time, compare them. if all ==, then it is a palindrome
    	ListNode cur = head;
    	while(cur != null) {
    		stack.push(cur.val);
    		cur = cur.next;
    	}
    	while(head != null) {
    		stackVal = stack.pop();
    		if(head.val == stackVal) {
    			isPalindrome = true;    			
    		}
    		else {
    			isPalindrome = false;
    			break;
    		}
    		head = head.next;
    	}
    	return isPalindrome;
    }
}