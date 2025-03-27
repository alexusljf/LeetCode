class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i in range(len(nums)):
            if target - nums[i] in pairs:
                return [i, pairs.get(target-nums[i])]
            else:
                pairs[nums[i]] = i
            print(pairs)
        return []