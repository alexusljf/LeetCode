class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i,j;
        int[] result = new int[2];
        for(i=0;i<nums.length;i++) {
        	for(j=0;j<nums.length;j++) {
        		if(i==j) {
        			continue;
        		}
        		else {
        			if(nums[i] + nums[j] == target) {
        				result[0] = i;
        				result[1] = j;
        				break;
        			}
        		}
        	}
        }
        return result;
    }
}