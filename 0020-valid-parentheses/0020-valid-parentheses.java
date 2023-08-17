class Solution {
    public boolean isValid(String s) {
        char[] sArray = s.toCharArray();
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < sArray.length; i++) {
            // push all the open paranthesis into stack
            if ((sArray[i] == '(') || (sArray[i] == '[') || (sArray[i] == '{')) {
                stack.push(sArray[i]);
            }
            // if current char is closing paranthesis, then we check if stack contains the
            // corresponding opening paranthesis, if yes then pop out. else is not valid
            if ((sArray[i] == ')') || (sArray[i] == ']') || (sArray[i] == '}')) {
                // check for case when stack is empty
                if (stack.isEmpty()) {
                    return false;
                }
                if ((sArray[i] == ')') && (stack.peek() == '(')) {
                    stack.pop();
                } else if ((sArray[i] == '}') && (stack.peek() == '{')) {
                    stack.pop();
                } else if ((sArray[i] == ']') && (stack.peek() == '[')) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        // if stack is not empty, means there are extra opening paranthesis and not
        // valid
        if (!stack.isEmpty()) {
            return false;
        }
        // if stack is empty, then matched all pairs of paranthesis, valid
        return true;
    }
}