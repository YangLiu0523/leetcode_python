#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-02-28 23:31:29

import string


class Solution:
    def _operations_and_nums(self, input):
        operations, nums = [], []
        s = ''
        for c in input + '\0':
            if c in string.digits:
                s += c
            else:
                nums.append(int(s))
                s = ''
            if c in '+-*/':
                operations.append(c)
        return operations, nums

    def _operate(self, oper, i, j):
        if oper == '+':
            return i + j
        elif oper == '-':
            return i - j
        elif oper == '*':
            return i * j
        else:
            raise Exception

    def _helper(self, operations, nums):
        if len(nums) <= 1:
            return [sum(nums)]
        first_two = self._operate(operations[0], nums[0], nums[1])
        if len(nums) == 2:
            return [first_two]

        result = []
        for index in range(len(operations)):
            oper = operations[index]
            lefts = self._helper(operations[:index], nums[:index+1])
            rights = self._helper(operations[index+1:], nums[index+1:])
            for i in lefts:
                for j in rights:
                    result.append(self._operate(oper, i, j))

        return result

    def diffWaysToCompute(self, input: str) -> List[int]:
        operations, nums = self._operations_and_nums(input)

        return self._helper(operations, nums)
