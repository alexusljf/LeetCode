class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        brackets = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets:
                if stack == []:
                    return False
                elif stack.pop() != brackets[char]:
                    return False
        return stack == []
        