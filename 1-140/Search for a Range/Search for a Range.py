class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            index1 = nums.index(target)
        except:
            index1 = -1
        
        nums = nums[::-1]
        
        try:
            index2 = len(nums) - nums.index(target) -1
        except:
            index2 = -1
        
        if index1 == -1 or index2 == -1:
            return [-1,-1]
        else:
            return [index1,index2]
