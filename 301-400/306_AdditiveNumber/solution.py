#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-02 21:33:29


class Solution:
    def _helper(self, s, x, y):
        if not s:
            return False

        index = len(s)
        while index > 0:
            diff = y - x
            if s[index-len(str(diff)):index] == str(diff):
                index -= len(str(diff))
                x, y = diff, x
            else:
                return False
        return True

    def isAdditiveNumber(self, num: str) -> bool:
        l = len(num)
        for l2 in range(1, l // 2 + 1):
            for l1 in range(1, l - l2):
                y = int(num[l - l2:l])
                x = int(num[l - l2 - l1:l - l2])
                if str(y) != num[l - l2:l] or str(x) != num[l - l2 - l1:l - l2]:
                    continue
                if self._helper(num[:l - l2 - l1], x, y):
                    return True
        return False


def main():
    testcases = [
        ('112358', True),
        ('199100199', True),
        ('113', False),
        ('0', False),
        ('5813', True),
        ('10', False),
        ('1203', False),
        ("199111992", True)
    ]
    for case, target in testcases:
        assert Solution().isAdditiveNumber(case) == target, "%s %s" % (case, target)

    print("All test passed")


if __name__ == '__main__':
    main()
