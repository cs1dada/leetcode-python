# Time:  O(n)
# Space: O(1)

# Given a string and an integer k, you need to reverse the first k characters
# for every 2k characters counting from the start of the string.
# If there are less than k characters left, reverse all of them.
# If there are less than 2k but greater than or equal to k characters,
# then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]
#
# tag: String
#

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stringBuf = list(s)
        print(stringBuf)
        for elem in range(0, len(stringBuf), 2*k):
            #print(elem)
            stringBuf[elem:elem+k] = list(reversed(stringBuf[elem:elem+k]))        
            #print(stringBuf[elem:elem+k])
            #print(list(reversed(stringBuf[elem:elem+k])))
            #print(stringBuf[elem:elem+2*k])
        return "".join(stringBuf)

if __name__ == "__main__":
    print(Solution().reverseStr("hellomynameisdaniel",2))                        

