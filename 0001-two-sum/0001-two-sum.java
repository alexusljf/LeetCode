class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create hashmap to store values and their indexes, then iterate thru array and check if need is in HashMap.
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int[] returnArray = new int[2];
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }
        for(int i = 0; i < nums.length; i++){
            int need = target - nums[i];
            if(map.containsKey(need) && map.get(need) != i){ // && condition checks if it's the same number
                returnArray[0] = i;
                returnArray[1] = map.get(need);
            }
        }
        return returnArray;
    }
}