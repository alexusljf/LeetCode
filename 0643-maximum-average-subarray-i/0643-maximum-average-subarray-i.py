class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k
        currentSum = sum(nums[:k])
        result = currentSum
        while r < len(nums):
            # update the currentSum instead of recalculating it
            currentSum += nums[r] - nums[l]
            # print(f'currentSum: {currentSum}, subarray:{nums[l:r]}')
            result = max(result, currentSum)
            r += 1
            l += 1
        return result / k
