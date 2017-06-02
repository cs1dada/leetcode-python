'''
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
'''
#
# tag: string
#

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        charBuf = s.split()
        return len(charBuf)

if __name__ == "__main__":
    print(Solution().countSegments("Hello, my name is John"))