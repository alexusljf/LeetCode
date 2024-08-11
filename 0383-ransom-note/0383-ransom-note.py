class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        check = [0] * 26
        for char in magazine:
            check[ord(char)-97] += 1
        for char in ransomNote:
            check[ord(char)-97] -= 1
        for char in check:
            if char < 0:
                return False
        return True