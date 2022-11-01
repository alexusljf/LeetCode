class Solution {
    public int removeDuplicates(int[] nums) {
    	int k = 0;
    	for(int i = 0; i < nums.length; i++) {
    		// if duplicate we ignore it and continue, else we put the different numbers together and increment k
    		if( (i < nums.length - 1) && nums[i] == nums[i+1]) {
    			continue;
    		}
    		else {
    			nums[k] = nums[i];
    			k++;
    		}
    	}
    	return k;
    }
}