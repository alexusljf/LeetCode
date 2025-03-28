class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = float('-inf')
        l,r=0,len(height)-1
        while l<r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
            # update the smaller height for chance to get bigger area
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return res