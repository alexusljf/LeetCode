class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # iterate thru both strings, increment i when the chars match
        if not s:
            return True
        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
                if (i == len(s)):
                    return True 
        # print(f'i: {i}, j: {j}')
        # if i != len(s), unable to iterate thru whole string as some char in the middle didnt match
        return False