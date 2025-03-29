class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # check if (length of substring - frequency of dominant char <= k)
        # if true then we can swap the chars to return substring of 1 char
        # else we increment l
        l=0
        res = 0
        seen = {}
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) +1
            maxfrequency = max(seen.values())
            if r-l+1 - maxfrequency > k: # means its not possible to turn this substring to 1 char
                seen[s[l]] -= 1
                l+=1
            r+=1
            res = max(r-l,res)
        return res
