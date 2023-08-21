/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int minDepth(TreeNode root) {
        // base case return 0
        if(root == null){
            return 0;
        }
        // as we go down the tree, increment depth by 1
        int min = 1;
        // for cases where only 1 child, 
        if(root.left == null){
            return min + minDepth(root.right);
        }
        if(root.right == null){
            return min + minDepth(root.left);
        }        
        return min += Math.min(minDepth(root.left), minDepth(root.right));
    }
    
}