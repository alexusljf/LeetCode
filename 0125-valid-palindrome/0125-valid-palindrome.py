class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean the string by removing non-alphanumeric chars and lowercase all chars
        sClean = ''.join(char.lower() for char in s if char.isalnum())
        print(sClean)
        l,r=0,len(sClean)-1
        while l<r:
            if sClean[l] != sClean[r]:
                return False
            l+=1
            r-=1
        return True