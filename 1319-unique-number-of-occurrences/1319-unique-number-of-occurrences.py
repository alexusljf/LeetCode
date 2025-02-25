class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashset = {}
        # store the occurence
        for i in arr:
            if i not in hashset:
                hashset[i] = 1
            else:
                hashset[i]+=1
        occurences = sorted(hashset.values())
        for i in range(1,len(occurences)):
            if occurences[i] == occurences[i-1]:
                return False
        return True