class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            chars = sorted(list(string))
            key = ''.join(chars)
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
        return list(anagrams.values())