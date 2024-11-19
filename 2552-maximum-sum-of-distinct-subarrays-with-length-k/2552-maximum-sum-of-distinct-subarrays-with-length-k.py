class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # return max sum of subarray of length k
        # use sliding window to iterate thru nums
        left = 0 
        right = 0
        result = 0
        currentSum = 0
        # seen set will track seen items, if we encounter a seen object, we remove from the subarray
        seen = set()
        for right in range(len(nums)):
            while nums[right] in seen:
                # remove from left until no duplicates
                currentSum -= nums[left]
                seen.remove(nums[left])
                left += 1
            seen.add(nums[right])
            currentSum += nums[right]
            if right - left + 1 == k:
                result = max(result, currentSum)
                # Slide the window by removing the leftmost element
                seen.remove(nums[left])
                currentSum -= nums[left]
                left += 1
        return result