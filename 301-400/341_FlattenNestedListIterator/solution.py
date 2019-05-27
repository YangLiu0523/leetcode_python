#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-27 23:13:12


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):
    def _dfs_init(self, node):
        if node.isInteger():
            self.data.append(node.getInteger())
        else:
            for child in node.getList():
                self._dfs_init(child)

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.data = []
        self.index = 0
        for node in nestedList:
            self._dfs_init(node)
        # self._dfs_init(nestedList)

    def next(self):
        """
        :rtype: int
        """
        i = self.index
        self.index += 1
        return self.data[i]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.data)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
