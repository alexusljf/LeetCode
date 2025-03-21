class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [0] * 2
        # res[0] contains all in num1 not in nums2
        # res[1] contian all in num2 not in num1
        distinctNums1 = set(nums1)
        distinctNums2 = set(nums2)
        res[0] = list(distinctNums1.difference(distinctNums2))
        res[1] = list(distinctNums2.difference(distinctNums1))
        return res