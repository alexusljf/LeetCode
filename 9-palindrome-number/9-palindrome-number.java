class Solution {
    public boolean isPalindrome(int x) {
    	// Convert to String -> Convert to char array
    	String number = String.valueOf(x);
    	char[] array = number.toCharArray();
        boolean palindrome = true;
        // Use For-Loop to compare the front item, with the back item.
        // If equals, then is palindome, else break and return false
        for(int i=0;i<array.length;i++) {
        	if(array[i] == array[array.length - 1 - i])
        		palindrome = true;
        	else {
        		palindrome = false;
        		break;
        	}
    }
		return palindrome;
    }
}