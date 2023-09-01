class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        // key: item value, value: index
        // if key is contained in hashmap (dupe found) and their index difference <= k,
        // return true
        // else put item and new latest index into hashmap
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (hashMap.containsKey(nums[i]) && Math.abs(i - hashMap.get(nums[i])) <= k) {
                return true;
            }
            hashMap.put(nums[i], hashMap.getOrDefault(nums[i], 0) + i);
        }
        return false;
    }
}