class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # previously used 3 nested loop to scan thru which works here cause len <= 100
        # use greedy approach to remove 1st loop, since we can use the max val for the first loop
        res = 0
        left = nums[0]
        for j in range(1, len(nums)):
            if nums[j] > left: # overwrite the left ptr if nums[j] > left
                left = nums[j]
                continue
            for k in range(j+1, len(nums)):
                res = max(res,(left-nums[j])*nums[k])
        return res