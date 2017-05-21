# Time:  O(n)
# Space: O(n)

# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
#  (ie, from left to right, level by level from leaf to root).
# 
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
# tag: Tree + Breadth-first Search
#

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
            
        currLevelStack = []
        result = []

        currLevelStack.append(root)
        while currLevelStack:
            levelBuf = []
            nextLevelStack = []

            for elem in currLevelStack:
                #print(elem.val)
                levelBuf.append(elem.val)
                if elem.left:
                    nextLevelStack.append(elem.left)
                if elem.right:
                    nextLevelStack.append(elem.right)

            #print(levelBuf)
            result.append(levelBuf)
            currLevelStack = nextLevelStack

        #return result[::-1]
        return list(reversed(result))


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    #result = Solution().levelOrderBottom(root)
    #for elem in result:
    #    print(elem)
    print(Solution().levelOrderBottom(root))