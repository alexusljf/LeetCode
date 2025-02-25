class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))
        result = ''
        for i in range(minLen):
            result += word1[i]
            result += word2[i]
        if minLen < len(word1):
            result += word1[minLen:]
        else:
            result += word2[minLen:]
        return result
            