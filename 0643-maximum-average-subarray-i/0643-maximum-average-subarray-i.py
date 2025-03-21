class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # two pointer to track k items
        l,r = 0,k
        # init res to be sum of first k items
        currentSum = sum(nums[l:r])
        res = currentSum
        while r<len(nums):
            currentSum = currentSum + nums[r] - nums[l]
            res = max(res,currentSum)
            l+=1
            r+=1
        return res/k