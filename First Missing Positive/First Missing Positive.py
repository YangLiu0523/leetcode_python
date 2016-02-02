import copy
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        marks = []
        for i in range(len(nums)):
            marks.append(0)
        
        marks.append(0)
        
        for i in nums:
            if i > 0 and i <= len(nums) :
                marks[i-1] = 1
        
        try:
            return marks.index(0)+1
        except:
            return 1
