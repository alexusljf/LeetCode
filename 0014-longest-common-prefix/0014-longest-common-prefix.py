class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        # set first string to prefix, check if the prefix starts at front of eacch string.
        # if not, we remove last char of prefix and try again
        for i in range(1,len(strs)):
            while(strs[i].find(prefix) != 0):
                prefix = prefix[0:len(prefix) - 1]
        return prefix