import java.util.ArrayList;
    class Solution {
	    public boolean canConstruct(String ransomNote, String magazine) {	
	    	int i = ransomNote.length();
	    	int check = 0;
	    	
	    	// Use ArrayLists because I want to remove the matching character once found
	    	// Use String.toCharArray() to convert String to Char Array then use a For-Each loop to add each char to the ArrayList
	    	ArrayList<Character> ransom = new ArrayList<Character>();
	    	for (char c : ransomNote.toCharArray()) {
	    	  ransom.add(c);
	    	}
	    	ArrayList<Character> mag = new ArrayList<Character>();
	    	for (char c : magazine.toCharArray()) {
	    	  mag.add(c);
	    	}	    	
	    	for(int k = 0; k < ransom.size(); k++) {
	    		for(int j = 0; j < mag.size(); j++) {
	    			// If match, remove
	    			if(ransom.get(k)==mag.get(j)) {
	    				//ransom.remove(k);
	    				mag.remove(j);
	    				check++;
                        break;
                    }
	    		}
	    	}
	    	return (check == i);
	    }
	}