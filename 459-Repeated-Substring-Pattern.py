class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) == 1:
            return False

        trimChar = sorted(set(s))
        trimLength = len(trimChar)

        if len(s) % trimLength != 0:
            return False
            
        trimChar = list(trimChar)
        trimChar = trimChar * int(len(s)/trimLength)
        trimChar = "".join(trimChar)
        #print(trimChar)

        if trimChar == s:
            return True
        else:
            return False

    def repeatedSubstringPattern2(self, str):            
        if not str:
            return False
            
        ss = (str + str)[1:-1]
        return ss.find(str) != -1


if __name__ == "__main__":
    #print(Solution().repeatedSubstringPattern("abcabcabcabc"))
    print(Solution().repeatedSubstringPattern2("abcabcabcabc"))