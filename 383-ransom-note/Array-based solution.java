import java.util.ArrayList;
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) { 
        int[] m = new int[26];
        
        // Create an array, each index represents each alphabet
        // get the char then -97 to get the index (eg: 'a' is 97 in ASCII)
        // increment: count of letters available in magazine
        // decrement: number of letters needed in ransomNote
        // if any alphabet is <0, means that not enough letter in magazine for ransomNote
        
        for (int i = 0; i<magazine.length(); i++) {
            m[magazine.charAt(i) - 97]++;
        }
        
        for (int i = 0; i<ransomNote.length(); i++) {
            m[ransomNote.charAt(i) - 97]--;
        }
        
        for (int i = 0; i<26; i++) {
            if (m[i] < 0) {
                return false;
            }
        }
        
        return true;
    }
}