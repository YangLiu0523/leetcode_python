class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for i in nums:
            count[i]+=1
        
        num = 0
        i = 0
        while count != [0,0,0]:
            if count[num] == 0:
                num += 1
                continue
            nums[i] = num
            i += 1
            count[num] -= 1
        
            
