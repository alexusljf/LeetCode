class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = dict()
        for i,num in enumerate(nums):
            if num in hashMap:
                if i-hashMap[num] <= k:
                    return True
            hashMap[num] = i
        return False