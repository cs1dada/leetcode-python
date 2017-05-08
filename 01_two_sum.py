# Time:  O(n)
# Space: O(n)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
# tag: hash table + array
#
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        bucket = {} #dict ('key':value, ...)
        for index, elem in enumerate(nums):
            if target - elem in bucket:
                return [bucket[target - elem], index]
            else:
                bucket[elem] = index

        return [] # no two sum




if __name__ == '__main__':
    print(Solution().twoSum((2, 7, 11, 15), 9))