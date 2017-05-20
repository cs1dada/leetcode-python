# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
# such that adding up all the values along the path equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#
# tag: Tree + Depth-first Search
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #simple recursive
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        # leaf
        if root.left is None and root.right is None and root.val == sum:
            return True

        sum = sum - root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


    # ref 257-binary-tree-paths
    def hasPathSum2(self, root, summary):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        result = []
        path =[]
        self.binaryTreePathsRecu2(root, path, result)
        #print(result)
        for elem in result:
            if summary == sum(elem):
                #print(summary)
                return True
        return False

    def binaryTreePathsRecu2(self, node, path, result):
        if node is None:
            return

        #leaf
        if node.left is None and node.right is None:
            listpath = []
            path.append(node)
            for n in path:
                listpath.append(n.val)
            result.append(listpath)
            path.pop()

        if node.left:
            path.append(node)
            self.binaryTreePathsRecu2(node.left, path, result)
            path.pop()

        if node.right:
            path.append(node)
            self.binaryTreePathsRecu2(node.right, path, result)
            path.pop()       



if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.right = TreeNode(2)
    print(Solution().hasPathSum(root, 23))            

'''
            5
           / \
          4   8
         /
        11
         \
          2
'''