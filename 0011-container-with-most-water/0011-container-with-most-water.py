class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left,area=0,0
        # for r in range(len(height)-1):
        #     for j in range(r+1,len(height)):
        #         area = max(area,min(height[r],height[j]) * (j-r))
        # return area
        
        left,right = 0,len(height)-1
        area = min(height[left],height[right])*(right-left)
        while left<right:
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
            area = max(area,min(height[left],height[right]) * (right-left))
        return area