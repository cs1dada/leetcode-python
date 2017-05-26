# Time:  O(n * k), k is the length of the common prefix
# Space: O(1)

# Write a function to find the longest common prefix string
# amongst an array of strings.
#
# tag: String
#

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strBuf = strs[0]
        print(len(strBuf))
        for index in range(len(strBuf)):
            for elem in strs[1:]: # compare "hello" with "heaven", "heavy"
                #print("elem:{}, elem[{}]:{}, strBuf[{}]:{}".format(elem, index, elem[index], index, strBuf[index]))
                if index >= len(elem) or elem[index] != strBuf[index]:
                    return strBuf[:index]
        return strBuf


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["aa","a"]))