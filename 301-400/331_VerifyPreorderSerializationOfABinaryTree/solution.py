#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-22 21:48:53


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = [0]
        for node in preorder.split(','):
            if node != '#':
                stack.append(0)
            else:
                if not stack:
                    return False
                stack[-1] += 1
                while stack[-1] == 2:
                    stack.pop()
                    if not stack:
                        return False
                    stack[-1] += 1

        return stack == [1]
