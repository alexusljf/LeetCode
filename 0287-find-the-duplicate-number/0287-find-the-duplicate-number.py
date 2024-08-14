class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                return num
        