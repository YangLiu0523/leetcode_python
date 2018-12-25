#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-12-25 21:25:57
"""
"""
class Solution:
    pass


if __name__ == '__main__':
    from sample import cases
    for args, result in cases:
        print("Running with case:", args, result)
        assert Solution().isIsomorphic(*args) == result
