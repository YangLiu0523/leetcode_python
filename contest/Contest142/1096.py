#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-23 19:53:28


class Solution:
    def _split(self, expr):
        expr = expr[1:-1]
        l = 0
        s = ''
        ans = []
        for c in expr:
            if l == 0 and c == ',':
                ans.append(s)
                s = ''
                continue
            if c == '{':
                l += 1
            elif c == '}':
                l -= 1
            s += c
        if s:
            ans.append(s)
        return ans

    def braceExpansionII(self, expr: str) -> List[str]:
        if '{' not in expr:
            return [expr]
        start = expr.index('{')
        end = start
        l = 1
        while l != 0:
            end += 1
            if expr[end] == '{':
                l += 1
            elif expr[end] == '}':
                l -= 1

        left = self.braceExpansionII(expr[end+1:])
        r = expr[:start]
        pos = self._split(expr[start:end + 1])
        ans = []
        for m in pos:
            for s in self.braceExpansionII(m):
                for l in left:
                    tmp = r + s + l
                    if tmp not in ans:
                        ans.append(tmp)
        l = max(len(s) for s in ans)
        ans.sort(key=lambda s:((s+'0' * l)[:l]))
        return ans
