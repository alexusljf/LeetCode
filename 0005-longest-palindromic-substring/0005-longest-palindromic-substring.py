class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        def helper(l,r,s):
            palindrome = ''
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    cur = s[l:r+1]
                    if len(cur) > len(palindrome):
                        palindrome = cur
                    
                    l-=1
                    r+=1
                else:
                    return palindrome
            return palindrome
        # iterate each character and expand to see if palindrome
        for i in range(len(s)):
            oddPalindrome = helper(i,i,s)
            evenPalindrome = helper(i,i+1,s)
            oddLonger = len(oddPalindrome) > len(evenPalindrome)
            if oddLonger and len(oddPalindrome) > len(res):
                res = oddPalindrome
            if not oddLonger and len(evenPalindrome) > len(res):
                res = evenPalindrome
        return res

