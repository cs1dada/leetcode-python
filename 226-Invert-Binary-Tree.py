# Time:  O(n)
# Space: O(h)
#
# Invert a binary tree.
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
#
# tag: tree
#

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #recursive
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            buf = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(buf)

        return root

    #iterative + stack
    def invertTree2(self, root):
        if root: #沒這行 root = None 會出錯
            stack = []
            stack.append(root)

            while stack:
                elem = stack.pop()
                elem.left, elem.right = elem.right, elem.left

                if elem.left:
                    stack.append(elem.left)
                if elem.right:
                    stack.append(elem.right)
        return root


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)

    test = Solution().invertTree(root)
    print(test.val)
    #print(test.left.val)
    print(test.right.val)
    #print(test.right.right.val)

        