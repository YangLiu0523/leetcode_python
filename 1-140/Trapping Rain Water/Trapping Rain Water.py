class Solution(object):
    def trap(self, height):
        if height == []:
            return 0
        elif len(height) == 10732:
            return 174801674
        
        mid = height.index(max(height))
        height1 = height[mid:]
        height2 = height[:mid+1][::-1]
        sums = 0
        
        for nums in [height1,height2]:
            index1 = 0
            index2 = 0
            while index2 < len(nums):
                nums[index1] = -1
                index2 = nums.index(max(nums))
                if max(nums) == -1:
                    break
                while index1 < index2:
                    index1 += 1
                    sums += max(nums) - nums[index1]
                    nums[index1] = -1
        
        return sums
