class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0; //pointer to track position of last-swapped
        // if cur != val, swap itself (no change, just ++ i)
        // else swap val with cur
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != val) {
                int tempInt = nums[i];
                nums[i] = nums[j];
                nums[j] = tempInt;
                i++;
            }
        }
        return i;
    }
}