'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and 
node values with a subtree of s. 

A subtree of s is a tree consists of a node in s and all of this node's descendants. 
The tree s could also be considered as a subtree of itself.

 tag: Tree

'''

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t is None:
            return True
        if s is None:
            return False

        if self.recurCheck(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def recurCheck(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False

        if root1.val == root2.val:
            return self.recurCheck(root1.left, root2.left) and self.recurCheck(root1.right, root2.right)
        else:
            return False
    '''
     Tree T is a subtree of S if both inorder and preorder traversals of T are 
     substrings of inorder and preorder traversals of S respectively.
    '''
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)

    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    print (Solution().isSubtree(root, subRoot))
'''
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

===================================
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

'''        