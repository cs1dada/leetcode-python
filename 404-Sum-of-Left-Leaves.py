# Time:  O(n)
# Space: O(h)

# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#    3
#   / \
#   9  20
#     /  \
#   15   7
#
# There are two left leaves in the binary tree,
# with values 9 and 15 respectively. Return 24.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return self.check(root, False)

    def check(self, node, isLeft):
        # leaf's child
        if node is None:
            return 0
        # left leaf
        if node.left is None and node.right is None and isLeft:
            return node.val
        # right leaf
        if node.left is None and node.right is None and not isLeft:
            return 0
        # internal node
        return self.check(node.left, True) + self.check(node.right, False)

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().sumOfLeftLeaves(root))

