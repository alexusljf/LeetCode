​Faster solution I found on the LeetCode discussions

class Solution {
    public int lengthOfLastWord(String s) {
        String trim = s.trim();
        int afterLastSpaceIndex = trim.lastIndexOf(' ') + 1;
        return trim.length() - afterLastSpaceIndex;
    }
}

Trim away any unwanted whitespaces at the front or back of String s
Use .lastIndexOf(' ') to find the last ' ' before the last word.
The length of the whole String s - that Last Index + 1 will return the length of the object (+ 1 because Length - Last Index is like the index)
