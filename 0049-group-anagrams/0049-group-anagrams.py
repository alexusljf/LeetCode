class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for str in strs:
            charList = sorted(list(str))
            print(charList)
            key = ''.join(charList)
            print(key)
            if key in anagramMap:
                anagramMap[key].append(str)
            else:
                anagramMap[key] = [str]
        
        print(anagramMap)
        return anagramMap.values()
            
            