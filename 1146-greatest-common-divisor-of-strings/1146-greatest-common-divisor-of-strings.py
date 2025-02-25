class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # gcd can % == 0 both strings
        # iterate thru all substrings and check if each can divide str 1 and str 2
        for i in range(min(len(str1), len(str2)),0,-1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                gcd = str1[:i]
            # check if gcd can be repeated len/i times to form the string
                if gcd * (len(str1)//i) == str1 and gcd * (len(str2)//i) == str2:
                    return gcd
        return ''
