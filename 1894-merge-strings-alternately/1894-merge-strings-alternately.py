class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        lenWord1 = len(word1)
        lenWord2 = len(word2)
        for i in range(min(lenWord1, lenWord2)):
            res += word1[i]
            res += word2[i]
            
        if lenWord1 < lenWord2:
            res += word2[lenWord1:]
        elif lenWord1 > lenWord2:
            res += word1[lenWord2:]

        return res