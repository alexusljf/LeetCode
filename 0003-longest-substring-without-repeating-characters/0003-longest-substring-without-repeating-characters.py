class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l=0
        seen=set() #store the seen chars
        for r in range(len(s)):
            while s[r] in seen: #if the incoming char is seen, remove the seen items until s[r] is not in
                seen.remove(s[l])
                l+=1
            seen.add(s[r]) #add each incoming char
            r+=1
            res = max(res, r-l)
        return res