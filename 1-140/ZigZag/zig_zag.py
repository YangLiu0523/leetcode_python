#!/usr/bin/python
# coding=utf-8
#
# Title:    ZigZag from TopCoder
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-19 22:14:14
#
class ZigZag(object):
    def longestZigZag(self, nums):
        flags = [nums[1] > nums[0]]
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] != 0 and flags[-1] != (nums[i+1] > nums[i]):
                flags.append(nums[i+1] > nums[i])
        return len(flags) + 1


if __name__ == '__main__':
    # case = [1, 7, 4, 9, 2, 5]
    case = [374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
            600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
            67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
            477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
            249, 22, 176, 279, 23, 22, 617, 462, 459, 244]
    print ZigZag().longestZigZag(case)
