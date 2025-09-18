"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # base case empty tree
        if not root:
            return 0
        # return depth 1 for leaf nodes
        if not root.children:
            return 1
        depths = []
        # since don't know how many children, use for loop to run the function n times
        for children in root.children:
            depths.append(self.maxDepth(children))
        return max(depths) + 1
        # can also use 'default = 0' if we dont use the if for leaf nodes
        # this prevents error when we run max on empty list
        # return max(depths, default=0) + 1
