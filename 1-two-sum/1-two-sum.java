class Solution {
public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        // Use HashMap for O(1) constant time access
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>(); // Syntax is Key, Value
    	int i;
    	for(i=0;i<nums.length;i++) {
    		// Key is item, value is index
    		map.put(nums[i], i);
    	}
        for(i=0;i<nums.length;i++) {
        	int need = target - nums[i];
        	if(map.containsKey(need) && map.get(need) != i) {
        			result[0] = i;
        			result[1] = map.get(need); // map.get(key) to get the index value
        		}
        	}        
        return result;
    }
}