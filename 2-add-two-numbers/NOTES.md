Tried this originally, works but there will be overflow issues when values get too big (eg: 1 + 999999991 gives a negative value)
I think BigInteger can fix this (it's a data type?) but didn't try. The other solution is faster too as it avoids repetition of multiplying and summing up.

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int val1 = 0, val2 = 0;
		ListNode tempNode = l1;
    
This part is repeated for L1 and L2

		for(int i = 0; tempNode != null; i++){
			val1 += (int) (tempNode.val * Math.pow(10.0,i ));
			tempNode = tempNode.next;
		}
		tempNode = l2;
		for(int i = 0; tempNode != null; i++){
			val2 += (int) (tempNode.val * Math.pow(10.0,i ));
			tempNode = tempNode.next;
		}
		 System.out.println(val1);
		 System.out.println(val2);
		ListNode returnNode = new ListNode(); // create a new LL
		tempNode = returnNode; // temp pointer
		int result = val1 + val2, i=0;
		 System.out.println(result);
		while(result!=0){
			int remainder = result % 10;
			ListNode temp2 = new ListNode(remainder);
			if(i == 0){
				returnNode = temp2;
			}
			tempNode.next = temp2;
			tempNode = tempNode.next;
			result = (result - remainder) / 10;
			i++;			
		}
		return returnNode;
    }
