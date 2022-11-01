class Solution {
    public String longestCommonPrefix(String[] strs) {
    	// Initialize the prefix as the entire first string
    	// Iterate through the String array and compare the prefix string with each string in the array
    	// If index.Of(prefix) != 0, this means that the prefix is not found at the start of the string
    	// Use .substring to remove the last char from the prefix string and check again
        String prefix = strs[0];
        for(int i = 1; i< strs.length; i++) {
        	while(strs[i].indexOf(prefix) != 0) {
        		prefix = prefix.substring(0, prefix.length() - 1);
        	}
        }
        // if prefix is empty, means we removed every letter and the prefix still does not start at index 0
        // this means there is no common prefix among all strings
        if(prefix.isEmpty()) {
        	return "";
        }
        else {
        	return prefix;
        }
    }
}