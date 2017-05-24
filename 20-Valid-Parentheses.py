# Time:  O(n)
# Space: O(n)
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" 
# are all valid but "(]" and "([)]" are not.
#
#
# tag: String + stack 
#

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, parenthess = [], {'(':')', '[':']', '{':'}'} #key:value
        for elem in s:
            if elem in parenthess.keys():
                stack.append(elem)
            elif elem in parenthess.values():
                if stack == [] or elem != parenthess[stack.pop()]:
                    return False
        if stack:
            return False
        else:
            return True


if __name__ == "__main__":
    print(Solution().isValid("]"))
    print(Solution().isValid("("))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("()[{]}"))
    print(Solution().isValid("(({[[()]]}))"))
