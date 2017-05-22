# Time:  O(n)
# Space: O(n)
#
# Write a function that takes a string as input and
# returns the string reversed.
#
# Example:
# Given s = "hello", return "olleh".
#
# tag: Two Pointers + String
#

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]