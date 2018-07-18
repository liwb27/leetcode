# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

# Example:

# Input:

#    1
#     \
#      3
#     /
#    2

# Output:
# 1

# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
# Note: There are at least two nodes in this BST.

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

# 和783题一样