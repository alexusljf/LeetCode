class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pivotLeftArr = [0] * n
        pivotLeftArr[0] = nums[0]
        for i in range(1, n):
            pivotLeftArr[i] = pivotLeftArr[i-1] + nums[i]
        print(pivotLeftArr)

        pivotRightArr = [0] * n
        # indexing of pivotRightArr same as LeftArr
        pivotRightArr[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            pivotRightArr[i] = pivotRightArr[i+1] + nums[i]
        print(pivotRightArr)

        for i in range(n):
            if pivotLeftArr[i] == pivotRightArr[i]:
                return i
        return -1