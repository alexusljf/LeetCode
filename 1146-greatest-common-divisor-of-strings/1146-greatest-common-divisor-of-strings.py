class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        lenStr1, lenStr2 = len(str1), len(str2)
        for i in range(min(lenStr1, lenStr2), 0, -1):
            if lenStr1 % i == 0 and lenStr2 % i == 0:
                #possible GCD
                GCD = str1[:i]
                if GCD * (lenStr1 // i) == str1 and GCD * (lenStr2 // i) == str2:
                    return GCD
        return ''