#!/usr/bin/env python
# coding=utf-8
#
# Title: 155. Min Stack
# Author: Lucas
# Date: 2018-05-29 21:29:35
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_stack and x > self.min_stack[-1]:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.min_stack.pop()
        return self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

