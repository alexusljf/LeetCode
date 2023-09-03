class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() > haystack.length()) {
            return -1;
        }
        int occurenceCount = 0;
        // for each char in haystack check if that letter is part of the needle
        for (int firstIndex = 0; firstIndex < haystack.length(); firstIndex++) {
            int tempIndex = firstIndex;
            System.out.println("Loop " + firstIndex);
            // only enter checking loop if current char match with 1st char of needle AND
            // enough space left in haystack to fit needle
            if ((haystack.charAt(firstIndex) == needle.charAt(0))
                    && ((haystack.length() - tempIndex + 1) > needle.length())) {
                for (int j = 0; j < needle.length(); j++) {
                    if (haystack.charAt(tempIndex) == needle.charAt(j)) {
                        System.out.println(haystack.charAt(tempIndex) + " " + tempIndex);
                        tempIndex++;
                        occurenceCount++;
                    }
                }
            } // matches with 1st letter of needle
            if (occurenceCount == needle.length()) { // if entire needle is found, return the index of needle start
                return firstIndex;
            } else { // else reset the occurence Count
                occurenceCount = 0;
            }
        }
        return -1; // return -1 if not found
    }
}
