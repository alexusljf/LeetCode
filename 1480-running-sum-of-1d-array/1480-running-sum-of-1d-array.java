class Solution {
    public int[] runningSum(int[] nums) {
        int numsLength = nums.length, i;
        for(i=1;i<numsLength;i++){
            nums[i] = nums[i] + nums[i-1];
        }
        return nums;
    }
}