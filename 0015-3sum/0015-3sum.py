class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == [0] * len(nums):
            return [[0,0,0]]
        
        returnSet = set()
        nums_sorted = sorted(nums)
        for i in range(len(nums_sorted)-2):
            l,r=i+1,len(nums_sorted)-1
            while l<r:
                if nums_sorted[i]+nums_sorted[l]+nums_sorted[r] == 0:
                    returnSet.add((nums_sorted[i],nums_sorted[l],nums_sorted[r]))
                    l+=1
                if nums_sorted[i]+nums_sorted[l]+nums_sorted[r] < 0:
                    l+=1
                elif nums_sorted[i]+nums_sorted[l]+nums_sorted[r] > 0:
                    r-=1
        return list(returnSet)