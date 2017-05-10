# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree 
# in which the depth of the two subtrees of every node never differ by more than 1.
#
# tag: Tree + Depth-first Search
#

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #leaf or empty tree
        if root is None:
            return True

        #check root's left and right subtree is balanced
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False

        # recurcive chcek left and right children are balance tree
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
        

    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print (Solution().isBalanced(root))

'''
3        1
        / \
2      2   3
      /     
1    4
    /
0 null

'''        