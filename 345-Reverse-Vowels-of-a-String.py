# Time:  O(n)
# Space: O(1)

# Write a function that takes a string as input 
# and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
# tag: Two Pointers + String
#

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a","e","i","o","u"]
        strBuf = list(s)
        head = 0
        tail = len(s) -1

        while head < tail:
            #only head move
            if strBuf[head].lower() not in vowels:
                head += 1
            #only tail move
            elif strBuf[tail].lower() not in vowels:
                tail -= 1
            else:
                #swap two vowel characters 
                strBuf[head], strBuf[tail] = strBuf[tail], strBuf[head]
                head += 1
                tail -= 1

        return "".join(strBuf)

if __name__ == "__main__":
    print(Solution().reverseVowels("hello"))





