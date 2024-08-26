class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        returnList = list()
        nums_sorted = sorted(nums)
        for i in range(len(nums_sorted)-2):
            if i >0 and  nums_sorted[i] == nums_sorted[i-1]:
                continue
            l,r=i+1,len(nums_sorted)-1
            while l<r:
                total = nums_sorted[i]+nums_sorted[l]+nums_sorted[r]
                if total == 0:
                    returnList.append((nums_sorted[i],nums_sorted[l],nums_sorted[r]))
                    l+=1
                    r-=1
                    while nums_sorted[l] == nums_sorted[l-1] and l<r:
                        l+=1
                if total < 0:
                    l+=1
                elif total > 0:
                    r-=1
        return returnList