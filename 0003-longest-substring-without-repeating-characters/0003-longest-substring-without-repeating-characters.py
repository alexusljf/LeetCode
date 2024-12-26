class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        substringStart, result = 0, 0
        # hash map to store char, index pair
        charMap = {}
        for r in range(len(s)):
            # if char is present in map and after the start of current substring, we set start position to after the previous occurence
            if s[r] in charMap and charMap[s[r]] >= substringStart:
                substringStart = charMap[s[r]] + 1
            # add the char:index pair to map
            charMap[s[r]] = r
            result = max(result, r - substringStart + 1)

        return result
