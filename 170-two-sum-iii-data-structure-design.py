# Time:  O(n)
# Space: O(n)

# Design and implement a TwoSum class. It should support the following operations: add and find.
# 
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
# 
# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
"""
#iterate in dict
for key in dict:
    print(key)       # return key not value
    print(dict[key]) # return value

"""

from collections import defaultdict

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.data = defaultdict(int)# create dict{"key":value(int)}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """        
        self.data[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """        
        for key in self.data:
            target = value - key
            if target in self.data and (target != key or self.data[key] > 1):
                return True

        return False


if __name__ == "__main__":
    Sol = TwoSum()
    
    for i in (1, 3, 5, 1):
        Sol.add(i)
    
    for i in (4, 7, 2):
        print(Sol.find(i))
                        