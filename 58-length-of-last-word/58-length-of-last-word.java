class Solution {
    public int lengthOfLastWord(String s) {
    	int count = 0; // Count of words
    	ArrayList<String> words  = new ArrayList<String>(); // ArrayList to store individual words
        for(String word : s.split(" ")) { // Split the string into smaller strings separated by " "
        	count++;
        	words.add(word);
        }
        return words.get(count - 1).length();
    }
}