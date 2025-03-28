class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create copy with only alphanumerics by using isalnum in list comprehension
        sClean = ''.join([char.lower() for char in s if char.isalnum()])
        l,r=0,len(sClean)-1
        while l<r:
            if sClean[l] != sClean[r]:
                return False
            l+=1
            r-=1
        return True