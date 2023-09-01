class Solution {
    public boolean containsDuplicate(int[] nums) {
        // loop thru array, add items to HashMap. if arraylist already contains item
        // then return true (there is dupe), else return false (no dupes found)
        HashMap<Integer, Integer> HashMap = new HashMap<Integer, Integer>(); // key: number, value: no. of occurence
        for (int i = 0; i < nums.length; i++) {
            if (HashMap.containsKey(nums[i]) && HashMap.get(nums[i]) >= 1) {
                return true;
            }
            // use getOrDefault as initially no value so get will cause error. (will get the
            // value of nums[i] or pass in default value of 0)
            // increment the value of the key
            HashMap.put(nums[i], HashMap.getOrDefault(nums[i], 0) + 1);
        }
        return false;
    }
}