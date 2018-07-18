# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

# Example :

# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.

# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

#           4
#         /   \
#       2      6
#      / \    
#     1   3  

# while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
# Note:

# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's value is different.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    prev_val = float('-inf')
    min_diff = float('inf')
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def evalue(node):
            if node.left != None:
                evalue(node.left)
            self.min_diff = min(self.min_diff, node.val - self.prev_val)
            self.prev_val = node.val
            if node.right != None:
                evalue(node.right)
        evalue(root)
        return self.min_diff

import random
# data = [random.randint(1,200) for _ in range(16)]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(Solution().minDiffInBST(root))

