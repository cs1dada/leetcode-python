# Time:  O(n)
# Space: O(1)

# You are given a string representing an attendance record for a student.
# The record only contains the following three characters:
#
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record
# doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
#
# You need to return whether the student could be rewarded according to his attendance record.
#
# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False
#
# tag: string 
#

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        charBuf = list(s)
        if charBuf.count("A") > 1:
            return False

        for index, elem in enumerate(charBuf):
            if index + 2 <= len(charBuf) - 1:
                if charBuf[index] == charBuf[index+1] == charBuf[index+2] == "L":
                    return False

        return True


if __name__ == "__main__":
    #print(Solution().checkRecord("PPALLP"))
    print(Solution().checkRecord("LALL"))
    print(Solution().checkRecord("PPALLL"))