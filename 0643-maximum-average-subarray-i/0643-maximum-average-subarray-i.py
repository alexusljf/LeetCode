class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = sum(nums[:k])
        result = currentSum
        for i in range(k,len(nums)):
            currentSum += nums[i]
            currentSum -= nums[i-k]
            result = max(currentSum, result)
        return result / k
