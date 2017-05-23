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
        #buffer
        strBuff = list(s)
        print(strBuff)
        #head
        base = 0
        #tail
        strLength = len(strBuff) -1
        #swap
        while base < strLength:
            strBuff[base], strBuff[strLength] = strBuff[strLength], strBuff[base]
            base += 1
            strLength -= 1

        return "".join(strBuff) #['o', 'l', 'l', 'e', 'h'] => olleh
        #return "".join(reversed(s))
        #return s[::-1]

if __name__ == "__main__":

    print(Solution().reverseString("hello"))            
