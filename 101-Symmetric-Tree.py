# Time:  O(n)
# Space: O(h), h is height of binary tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# 
# For example, this binary tree is symmetric:
# 
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#
# tag: Tree + Depth-first Search + Breadth-first Search
#

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #recursive
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.check(root.left, root.right)


    def check(self, leftNode, rightNode):
        if leftNode is None and rightNode is None:
            return True
        if leftNode is None or rightNode is None:
            return False

        if leftNode.val == rightNode.val:
            return self.check(leftNode.left, rightNode.right) and self.check(leftNode.right, rightNode.left)
        else:
            return False

    #iterative
    def isSymmetric2(self, root):
        stack = []
        
        if root is None:
            return True

        stack.append(root.left)
        stack.append(root.right)
        # stack |l|r
        while stack:
            # r
            buf1 = stack.pop()
            # l
            buf2 = stack.pop()

            if buf1 is None and buf2 is None:
                #return True // recursive才是 return ...
                continue

            if buf1 is None or buf2 is None:
                return False

            if buf1.val == buf2.val:
                # buf1  buf2
                #    \  /
                stack.append(buf1.left)
                stack.append(buf2.right)
                # buf1  buf2
                # /        \
                stack.append(buf1.right)
                stack.append(buf2.left)
            else:
                return False

        #don't forget...
        return True





