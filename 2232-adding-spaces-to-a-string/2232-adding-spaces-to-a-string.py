class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        # use 2 pointer, 1 to track s, 1 to track spaces
        j = 0
        for i,k in enumerate(s):
            # if current s == index to put a space, add space and increment space ptr
            if j < len(spaces) and i == spaces[j]:
                result.append(" ")
                j += 1
            result.append(k)
        print(result)
        return "".join(result)
        
            