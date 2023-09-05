i was almost there, mistake was the random  pointers were pointing to nodes with correct value, but not to the previously created node with that value

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }
        
        // First Pass: Create new nodes and link them to the original list
        Node cur = head;
        while (cur != null) {
            Node newNode = new Node(cur.val);
            newNode.next = cur.next; // Link the new node to the next node in the original list
            cur.next = newNode; // Link the original node to the new node
            cur = newNode.next; // Move to the next original node
        }
        
        // Second Pass: Assign random pointers for the new nodes
        cur = head;
        while (cur != null) {
            if (cur.random != null) {
                cur.next.random = cur.random.next; // Set random pointer for the new node
            }
            cur = cur.next.next; // Move to the next original node
        }
        
        // Third Pass: Separate the original list and the new list
        cur = head;
        Node newHead = head.next;
        Node newCur = newHead;
        while (cur != null) {
            cur.next = cur.next.next; // Unlink the original node
            if (newCur.next != null) {
                newCur.next = newCur.next.next; // Unlink the new node
            }
            cur = cur.next;
            newCur = newCur.next;
        }
        
        return newHead;
    }
}
