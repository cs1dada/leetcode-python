# Time:  O(1)
# Space: O(1)

# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#       ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.
#
#  tag: Bit Manipulation


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        xor_result = x^y
        #print(bin(xor_result))

        while xor_result > 0:
            if (xor_result & 1) > 0:
                distance += 1            
            xor_result = xor_result >> 1            
            #print(bin(xor_result), distance)

        return distance

    def hammingDistance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #str.count(sub[, start[, end]]) 計算 sub 出現的次數， 
        #start 為起始計算索引值， end 為結束索引值
        return bin(x ^ y).count('1')    

if __name__ == '__main__':
    print(Solution().hammingDistance2(1, 4))