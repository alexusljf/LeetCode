class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
    	int i;
    	int[] arrayOfOnes = new int [mat.length];
    	// Use NumberOfOnes * NumberOfRows + RowNumber, + RowNumber to help with ties between rows
    	for(i=0;i<mat.length;i++) {
    		arrayOfOnes[i] = returnOnes(mat[i]) * mat.length + i;
    	}
    	Arrays.sort(arrayOfOnes);
    	int[] returnArray = new int[k];
    	// % RowLength to get the RowNumber
        for(i=0;i<k;i++) {
        	returnArray[i] = arrayOfOnes[i] % mat.length;
        }
        return returnArray;
    }
    
    	// Helper function to retrieve number of Ones in each array
        public int returnOnes(int[] array) {
        	int numOnes=0, i;
        	for(i=0;i<array.length;i++) {
        		if(array[i] == 0) {
        			numOnes = i;
        			return numOnes;
        		}
        		else if(i == array.length - 1) {
        			return i+1;
        		}
        	}
        	return numOnes;
        }
}