from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        lo = 0
        hi = n + 1
        while True:
            index = (hi + lo) // 2
            c_gr = 0
            c_le = 0
            c_eq = 0
            for num in nums:
                if num > index:
                    c_gr += 1
                elif num == index:
                    c_eq += 1
                else:
                    c_le += 1
            if c_eq > 1:
                return index

            if c_gr > n - index:
                lo = index
            else:
                hi = index

def main():
    cases = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([1, 1], 1)
    ]
    for arg, target in cases:
        ans = Solution().findDuplicate(arg)
        assert ans == target, "%s %s!=%s" % (arg, ans, target)

if __name__ == '__main__':
    main()
