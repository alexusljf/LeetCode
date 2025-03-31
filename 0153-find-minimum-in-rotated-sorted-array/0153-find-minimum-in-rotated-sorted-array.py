class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res = nums[0]
        while l<=r:
            mid = (l+r)//2
            # base case where list is fully sorted
            if nums[l] <= nums[r]:
                res = min(res,nums[l])
                return res
            res = min(res,nums[mid])
            # check if the left half is sorted, pivot on right, min is somewhere right of mid
            if nums[l] <= nums[mid]:
                l = mid+1
            else:
                # else pivot on left, min is somewhere left of mid
                r = mid-1
        return res



        