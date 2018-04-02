// Given a binary tree, find its maximum depth.

// The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

// For example:
// Given binary tree [3,9,20,null,null,15,7],

//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its depth = 3.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int MaxDepth(TreeNode root) {
        if(root == null)
            return 0;
        int left = MaxDepth(root.left);
        int right = MaxDepth(root.right);
        if(left > right)
            return left+1;
        else
            return right+1;
    }
}