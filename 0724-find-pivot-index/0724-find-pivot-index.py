class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        # init prefixSumLeft to start with first value, Right to start with last value
        prefixSumLeft=[nums[0]] * n
        prefixSumRight=[nums[n-1]] * n
        for i in range(1,n):
            prefixSumLeft[i] = nums[i] + prefixSumLeft[i-1]
        for i in range(n-2,-1,-1):
            # start from 2nd last to 0th index
            prefixSumRight[i] = nums[i] + prefixSumRight[i+1] # i+1 since we counting backwards
        for i in range(n):
            # find the pivot index where both arr have same sum
            if prefixSumRight[i] == prefixSumLeft[i]:
                return i
        return -1
