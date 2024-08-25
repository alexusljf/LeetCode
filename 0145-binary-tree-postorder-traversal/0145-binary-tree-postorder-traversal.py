# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # need a helper function to recursively append to the returning list
        returnList = list()
        self.helper(root, returnList)
        return returnList

        
    def helper(self, node, array):
        if node is None:
            return
        self.helper(node.left, array)
        self.helper(node.right, array)
        array.append(node.val)