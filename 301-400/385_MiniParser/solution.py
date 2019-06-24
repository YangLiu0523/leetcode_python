#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-24 23:06:18


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if '[' not in s:
            return NestedInteger(int(s))
        elements = []
        l = 0
        tmp = ''
        for c in s:
            if c == '[' and l == 0:
                l += 1
            elif c == '[':
                l += 1
                tmp += c
            elif c == ']' and l == 1:
                l -= 1
                elements.append(tmp)
            elif c == ']':
                l -= 1
                tmp += c
            elif c == ',' and l == 1:
                elements.append(tmp)
                tmp = ''
            else:
                tmp += c
        elements = [elem for elem in elements if elem]
        # elements.append(tmp)
        ans = NestedInteger()
        for elem in elements:
            ans.add(self.deserialize(elem))
        return ans
