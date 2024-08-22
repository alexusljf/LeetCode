class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use a set to store unique chars, iterate thru s
        char_set = set()
        l,length = 0,0
        for r in range(len(s)):
            # if cur char is in the set, we remove all chars from left until the set contains no duplicates
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[r])
            length = max(length,r-l+1)
        return length
        