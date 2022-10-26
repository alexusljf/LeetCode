class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        // Key is remainder, value is index.
        map.put(0, -1); // This is the 'base' case where remainder is 0
        int sum = 0;
        for(int i = 0; i < nums.length; i++){
            sum += nums[i]; // Add each item to sum, i will also be number of items added
            int remainder = sum % k;

            if(map.containsKey(remainder) && i - map.get(remainder) > 1){ // if there is the remainder in the array, and at least 2 items not counting the remainder item, then return true
                return true;
            }
            if(map.containsKey(remainder) == false){
                map.put(remainder, i);
            }
        }
        return false;
    }
}