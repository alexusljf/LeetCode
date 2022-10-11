​My Original Solution, only works for positive numbers (>0)
Any number <0 or =0 will not do the while(x>0) loop, as such the ArrayList will be empty and will then return palindrome = true

import java.util.ArrayList;

class Solution {
    public boolean isPalindrome(int x) {
        ArrayList<Integer> AL = new ArrayList<Integer>();
        boolean palindrome = true;
        // Pass the digits into an ArrayList
        while(x > 0) {
        	AL.add(x % 10);
        	x /= 10;
        }
        // Use For-Loop to compare the front item, with the back item.
        // If equals, then is palindome, else break and return false
        for(int i=0;i<AL.size();i++) {
        	if(AL.get(i) == AL.get(AL.size()-1-i)) {
        		palindrome = true;
        	}
        	else {
        		palindrome = false;
        		break;
        	}
        }
        return palindrome;
    }
}
