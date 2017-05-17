# Time:  O(n)
# Space: O(1)/O(n)
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#   3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal, stack = [], [(root, False)]
        while stack:
            buf, visited = stack.pop()
            #LVR
            if visited:
                traversal.append(buf.val)
            else:                
                if buf.right is not None:
                    stack.append((buf.right, False))
                
                stack.append((buf, True))

                if buf.left is not None:
                    stack.append((buf.left, False))

        return traversal

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)

    print (Solution().inorderTraversal(root))
'''

Given tree s:

       3
      / 
     4   
    / 
   1  

Given tree s:

       3
      / \
     4   5
    / \
   1   2

stack:
[(3,f)]
[(5,f), (3,t), (4,f)]
[(5,f), (3,t), (2,f), (4,t), (1,f)]
[(5,f), (3,t), (2,f), (4,t), (1,t)]
[(5,f), (3,t), (2,f), (4,t)]         [1]
[(5,f), (3,t), (2,f)]                [1, 4]
[(5,f), (3,t), (2,t)]                [1, 4]
[(5,f), (3,t)]                       [1, 4, 2]
[(5,f)]                              [1, 4, 2, 3]
[(5,t)]                              [1, 4, 2, 3]
[]                                   [1, 4, 2, 3, 5]
'''
