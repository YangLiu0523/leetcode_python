class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        lengths = [0] * len(nums)
        for i in range(len(nums)):
            length = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    length = max(lengths[j] + 1, length)
            lengths[i] = length
        return max(lengths)
