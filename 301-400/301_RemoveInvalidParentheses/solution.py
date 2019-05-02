#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-02 20:01:39
from typing import List


class Solution:
    def __init__(self):
        self.string = None
        self.min_rem_count = None
        self.valid_strings = None

    def _reset(self, s):
        self.string = s
        self.min_rem_count = len(s)
        self.valid_strings = set()

    def _dfs(self, index, expr, l_count, r_count, rem_count):
        # If we meet the end of the string
        if index == len(self.string):
            if l_count == r_count and rem_count <= self.min_rem_count:
                if rem_count < self.min_rem_count:
                    self.min_rem_count = rem_count
                    self.valid_strings = set()
                self.valid_strings.add(''.join(expr))
            return

        # Optimize
        if rem_count > self.min_rem_count:
            return
        elif abs(l_count - r_count) > (len(self.string) - index):
            return

        # Body of this dfs
        c = self.string[index]
        if r_count > l_count:
            return
        if c not in '()':
            expr.append(c)
            self._dfs(index+1, expr, l_count, r_count, rem_count)
            expr.pop()
        else:
            self._dfs(index+1, expr, l_count, r_count, rem_count+1)
            if c == '(':
                expr.append(c)
                self._dfs(index+1, expr, l_count+1, r_count, rem_count)
                expr.pop()
            elif c == ')':
                expr.append(c)
                self._dfs(index+1, expr, l_count, r_count+1, rem_count)
                expr.pop()

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self._reset(s)
        self._dfs(0, [], 0, 0, 0)
        return list(self.valid_strings)


def main():
    testcases = [
        "(()",
        "(a)())()",
        ")("
    ]
    for case in testcases:
        print(case, Solution().removeInvalidParentheses(case))


if __name__ == '__main__':
    main()
