class Solution {
    public int maximumWealth(int[][] accounts) {
        int max=0, cur, i, j;
        for(i=0;i<accounts.length;i++) {
        	cur = 0;
        	for(j=0;j<accounts[i].length;j++) {
        		if(i==0) {
        			// first iteration, to get a max value first for comparison
        			max += accounts[i][j];
        		}
        		else {
        			cur += accounts[i][j];
        		}
        	}
        if(cur>max) {
        	max = cur;
        }
        }
        return max;
    }
}