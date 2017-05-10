# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# tag:  Tree + Depth-first Search + Breadth-first Search
#


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
            '''
            if parent do not have two children at same time, 
            error with min(minDepth,minDepth)

            2      1
                  / \
            1    2   3
                /     
            1  4
            '''
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print (Solution().minDepth(root))

'''
3      1
      / \
2    2   3
    /     
1  4
'''