class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = {}
        for char in s:
            sChars[char] = sChars.get(char, 0) + 1
        tChars = {}
        for char in t:
            tChars[char] = tChars.get(char, 0) + 1
        return tChars == sChars