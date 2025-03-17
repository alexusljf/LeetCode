class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        countValues = count.values()
        for value in countValues:
            if value % 2 != 0:
                return False
        return True