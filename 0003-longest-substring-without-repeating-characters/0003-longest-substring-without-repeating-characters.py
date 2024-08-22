class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        '''
        sliding window using set
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
        '''
        
        # sliding window using hashmap
        # use hashmap to store char, index pairs
        char_index_map = {}
        l,length=0,0
        for r in range(len(s)):
            # if the cur char is in the map and the index is within the sliding window (>=l), 
            # then we increment l to start after the prev occurence of the char
            if s[r] in char_index_map and char_index_map[s[r]] >= l:
                l = char_index_map[s[r]] + 1
            char_index_map[s[r]] = r
            length = max(length, r-l+1)
        return length