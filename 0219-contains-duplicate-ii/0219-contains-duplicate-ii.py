class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        firstIndex, secondIndex, check = 0,0,0
        hashMap = dict()
        for i, num in enumerate(nums):
            if num in hashMap:
                firstIndex = hashMap[num]
                secondIndex = i
                if(check == 0):
                    check = abs(firstIndex - secondIndex)
                else:
                    check = min(check,abs(firstIndex - secondIndex))
            hashMap[num] = i
        if check!=0:
            return check <= k
        else:
            return False

                
                
                
        