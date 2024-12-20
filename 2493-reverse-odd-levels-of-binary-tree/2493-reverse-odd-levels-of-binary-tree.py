# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        # DFS approach performs DFS on 2 nodes that will be swapped
        def DFS(left: Optional[TreeNode], right: Optional[TreeNode], level: int):
            if not left or not right:
                return None
            # swap the left and right values if level is odd
            if level % 2 == 1:
                # print(type(left))
                # print(type(right))
                temp = left.val
                left.val = right.val
                right.val = temp
            DFS(left.left, right.right, level+1)
            DFS(left.right, right.left, level+1)

        if root:
            DFS(root.left, root.right, 1)
        return root
        '''
        #BFS approach
        queue = deque([root])
        level = 0
        while queue:
            # level_size to track number of nodes per level. we pop those and append the current level's node to level_nodes and the children to the queue
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                level_nodes.append(cur)
            # perform the swapping
            if level % 2 == 1:
                i = 0
                j = len(level_nodes) - 1
                while i < j:
                    temp = level_nodes[i].val
                    level_nodes[i].val = level_nodes[j].val
                    level_nodes[j].val = temp
                    i += 1
                    j -= 1
            # increment the level after the swapping for current level
            level += 1
        return root