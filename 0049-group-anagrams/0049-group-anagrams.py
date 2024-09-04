class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for str in strs:
            key = tuple(sorted(str))
            if key not in anagramMap:
                anagramMap[key] = []
            anagramMap[key].append(str)
        return anagramMap.values()
            