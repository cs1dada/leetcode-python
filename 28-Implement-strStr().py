# Time:  O(n + k)
# Space: O(k)
#
# Implement strStr().
# 
# Returns a pointer to the first occurrence of needle in haystack,
#  or null if needle is not part of haystack.
#
#
# tag: string + two pointers
#
class Solution(object):
    # Time:  O(n * k)
    # Space: O(k)    
    # brute force
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenNeedle = len(needle)
        shift = len(haystack) - lenNeedle + 1 
        print("needle: " + needle)

        for elem in range(shift):
            print(haystack[elem:elem+lenNeedle])
            if haystack[elem:elem+lenNeedle] == needle:
                return elem
        return -1

    
if __name__ == "__main__":
    #print (Solution().strStr("a", ""))
    print (Solution().strStr("abababcdab", "ababcdx"))
    #print (Solution().strStr("\'\'\'\'", "\'\'\'\'"))    