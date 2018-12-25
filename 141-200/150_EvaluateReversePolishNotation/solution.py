#!/usr/bin/env python
# coding=utf-8
#
# Title: 150. Evaluate Reverse Polish Notation
# Author: Lucas
# Date: 2018-05-22 22:15:46
#
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for elem in tokens:
            if elem in '+-*/':
                b = int(stack.pop())
                a = int(stack.pop())
                if elem == '+':
                    stack.append(a + b)
                elif elem == '-':
                    stack.append(a - b)
                elif elem == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(elem))

        return stack[-1]
