class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in res:
                return [res.get(complement), i]
            res[nums[i]] = i
        return 0