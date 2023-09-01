    public ListNode reverseList(ListNode head) {
        ListNode cur = head;
        ListNode prev = null;
        ListNode next = null;
        while(cur!=null){
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        // prev will be the last node in the LL (the most right Node), cur will be null
        // prev will be start of the reversed LL
        return prev ;
    }