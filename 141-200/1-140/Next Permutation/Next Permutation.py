class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i>0:
            if nums[i]>nums[i-1]:
                break
            i-=1
        #print i
        
        sort_begin = i
        sort_end = len(nums) -1
        
        index = sort_end
        if i>0:
            while nums[index] <= nums[i-1]:
                index -= 1
            temp = nums[index]
            nums[index] = nums[i-1]
            nums[i-1] = temp
        
        while sort_end - sort_begin >= 1:
            temp = nums[sort_end]
            nums[sort_end] = nums[sort_begin]
            nums[sort_begin] = temp
            sort_end -= 1
            sort_begin += 1
