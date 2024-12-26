class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for i in range(len(word1) if len(word1) < len(word2) else len(word2)):
            result += word1[i] + word2[i]
        result += word1[len(word2):] if len(word2) < len(word1) else word2[len(word1):]

        return result
        