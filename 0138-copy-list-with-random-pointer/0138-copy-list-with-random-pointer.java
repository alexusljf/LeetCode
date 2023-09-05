/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if(head == null){
            return null;
        }
        // 1st loop, create new nodes with the same values as the original list and the same next pointers
        Node cur = head;
        while(cur!=null){
            Node newNode = new Node(cur.val);
            newNode.next=cur.next;
            cur.next=newNode;
            cur=newNode.next;
        }
        // setting the random pointer of each new node (cur.next) with the original's random pointer
        cur = head;
        while(cur!=null){
            if(cur.random!=null){
                // set to cur.random.next to point to the new copy of the random node
                cur.next.random = cur.random.next;
            }
                cur = cur.next.next;
            }
        // unlink the 2 lists by setting cur next to the next original
        // and new node's next to the next new node
        Node returnHead = head.next; // as head.next is the 1st new node
        Node newCur = returnHead;
        cur = head;
        while(cur!=null){
            cur.next = cur.next.next;
            if (newCur.next != null) {
                newCur.next = newCur.next.next;
            }
            cur=cur.next;
            newCur = newCur.next;
        }
        return returnHead;
    }
}