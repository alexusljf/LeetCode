"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.array = list()
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        for child in root.children:
            self.postorder(child)
        self.array.append(root.val)
        return self.array