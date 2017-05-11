# Time:  O(n * h)
# Space: O(h)
#
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#   1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
#
# tag:  Tree + Depth-first Search
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        self.binaryTreePathsRecu(root, "", result)
        return result
    
    def binaryTreePathsRecu(self, node, path, result):
        if node is None:
            return result

        if node.left is None and node.right is None:
            path = path + str(node.val)
            result.append(path)

        if node.left:
            #path = path + str(node.val) + "->"
            # error: ["1->2->5", "1->1->3"], node saves twice
            leftpath = path + str(node.val) + "->"
            self.binaryTreePathsRecu(node.left, leftpath, result)

        if node.right:
            rightpath = path + str(node.val) + "->"
            self.binaryTreePathsRecu(node.right, rightpath, result)



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print(Solution().binaryTreePaths(root))