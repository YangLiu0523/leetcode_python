#!/usr/bin/python
# coding=utf-8
#
# Title:    Jump Game II
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-07-30 16:09:56
#
class Solution(object):
    def jump(self, A):
        ret = last = curr = 0
        for i in range(len(A)):
            print i, ret, last, curr
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i+A[i])
        return ret


if __name__ == '__main__':
    # test_case = [2, 3, 1, 1, 4]
    test_case = [2, 3, 1, 1, 4, 2, 3, 1, 1, 4]
    print Solution().jump(test_case)
