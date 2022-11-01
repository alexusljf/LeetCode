class Solution {
    public boolean isValid(String s) {
    	// Base case, empty
    	if(s.isEmpty()) {
    		return false;
    	}
    	// Create a stack of characters
        Stack<Character> stack = new Stack<Character>();
    	for(int i = 0; i < s.length(); i++) {
    		// If open bracket, push to stack
    		if(s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{') {
    			stack.push(s.charAt(i));
    		}
    		// Else if close brackets
    		else {
    			// Base case, invalid
    			if(stack.isEmpty()) {
    				return false;
    			}
    			// Check, if there is valid pair, pop out of stack
    			if( (s.charAt(i) == ')' && stack.peek() == '(') || (s.charAt(i) == ']' && stack.peek() == '[') || (s.charAt(i) == '}' && stack.peek() == '{')){
    				stack.pop();
    			}
    			// If not valid, return false
    			else {
    				return false;
    			}
    		}
    	}
    	// If stack is empty, means popped out all valid pairs
    	if(stack.isEmpty()) {
    	return true;
    }
    	// Else if not empty, means there are some open brackets without any corresponding close brackets
    	else {
    		return false;
    	}
    }
}