from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = 0
        for hi in range(len(nums)):
            if nums[hi] != 0:
                nums[lo] = nums[hi]
                lo += 1

        for i in range(lo, len(nums)):
            nums[i] = 0


def main():
    cases = [
        [0, 1, 0, 3, 12],
    ]
    for case in cases:
        Solution().moveZeroes(case)
        print(case)


if __name__ == '__main__':
    main()
