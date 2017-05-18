# Time:  O(n)
# Space: O(logn)
#
# Given an array where elements are sorted in ascending order, 
# convert it to a height balanced BST.
#
# tag: Tree + Depth-first Search
#

'''
An empty tree is height-balanced. 
A non-empty binary tree T is balanced if:
1) Left subtree of T is balanced
2) Right subtree of T is balanced
3) The difference between heights of left subtree and right subtree is not more than 1.
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        
        pivot = len(nums) // 2

        root = TreeNode(nums[pivot])
        root.left = self.sortedArrayToBST(nums[:pivot])
        root.right = self.sortedArrayToBST(nums[pivot+1:])

        return root



if __name__ == "__main__":
    num = [1,2,3,4,5]
    result = Solution().sortedArrayToBST(num)
    print(result.val)
    print(result.left.val)
    print(result.right.val)        
    print(result.left.left.val)    
    #print(result.left.right.val)
    print(result.right.left.val)            
    #print(result.right.right.val)            

'''
    3
  2   5
1  0 4  0   
'''
