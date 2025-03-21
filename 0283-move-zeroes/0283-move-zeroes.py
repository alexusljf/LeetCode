class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # one to move thru nums, one to track where last non-0 should go
        lastNonZeroIndex = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                # swap to non-zero index
                nums[lastNonZeroIndex], nums[i] = nums[i], nums[lastNonZeroIndex]
                lastNonZeroIndex += 1
        