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

    def binaryTreePaths2(self, root):
        result, path = [], []
        self.binaryTreePathsRecu2(root, path, result)
        return result
    
    def binaryTreePathsRecu2(self, node, path, result):
        if node is None:
            return

        if node.left is node.right is None:
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
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.right = TreeNode(1)
    print(Solution().binaryTreePaths2(root))
    exclusivePath = Solution().binaryTreePaths2(root)

    maxExclusiveLen = 0
    for somepath in exclusivePath:
        if len(set(somepath)) > maxExclusiveLen:
            maxExclusiveLen = len(set(somepath))
    print(maxExclusiveLen)
