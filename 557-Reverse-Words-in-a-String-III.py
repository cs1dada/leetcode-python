# Time:  O(n)
# Space: O(1)

# Given a string, you need to reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and
# there will not be any extra space in the string.
#
# tag: String
#


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverseBuf = []
        # string -> list
        charBuf = s.split()
        #print(charBuf)

        for elem in charBuf:
            #(list -> string) - append -> list
            reverseBuf.append("".join(reversed(elem)))
        # list -> string
        return " ".join(reverseBuf)



if __name__ == "__main__":
    print(Solution().reverseWords("Let's take LeetCode contest"))