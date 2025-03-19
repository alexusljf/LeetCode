class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        operations = 0
        
        for i in range(len(nums)-2):
            if nums[i] == 0:
                self.helper(nums, i)
                operations += 1
        # if there is a 0 in the end array, then impossible so return -1 else return number of operations
        return -1 if 0 in nums else operations
    
    def helper(self, arr, start):
        # flips the 3 consecutive elements from start index
        for i in range(start, start + 3):
            arr[i] = 1 - arr[i]
                