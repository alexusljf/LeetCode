class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort nums to easily skip dupes
        nums.sort()
        for i in range(len(nums)-2):
            # skip if same number is being processed, continue to next iteration
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            # 2 ptr, update depending on sum
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    # store the valid triplet
                    res.append([nums[i], nums[l], nums[r]])
                    # skip if the next l or next r are dupes
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1   
                    l+=1
                    r-=1   
                elif sum <0:
                    l+=1
                else:
                    r-=1
        return res