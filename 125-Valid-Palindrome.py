'''
Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? 
This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''
#
# tag: string + two points
#

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True
            
        charBuf = []

        for elem in s:
            if elem.isalnum():
                charBuf.append(elem.lower())

        left = 0
        right = len(charBuf) - 1

        while (left < right):
            if (charBuf[left] != charBuf[right]):
                #print(charBuf[left] + charBuf[right])
                return False
            else:
                #print(charBuf[left] + charBuf[right])
                left += 1
                right -= 1
        
        return True