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
    public boolean isPalindrome(ListNode head) {
        boolean palindrome = true;
        Stack<Integer> stack = new Stack<Integer>();
        ListNode cur = head;
        while (cur != null) {
            stack.push(cur.val); // top of stack would be the end of the LL
            cur = cur.next;
        }
        while (head != null){
            if(head.val != stack.pop()){
                palindrome = false;
                break;
            }
            head = head.next;
        }
        return palindrome;
    }
}