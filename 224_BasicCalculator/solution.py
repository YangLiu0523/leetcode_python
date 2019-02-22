# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-22 23:25:28


import string


class Solution:
    def calculate(self, s: 'str') -> 'int':
        s = s.replace(' ', '')
        stack = []
        plus = True    # False is minus
        val = 0
        num = ''
        for c in s + '\0':
            if c in string.digits:
                num = num + c
            else:
                val += (1 if plus else -1) * (int(num) if num else 0)
                num = ''
            if c == '(':
                stack.append((val, plus))
                val, plus = 0, True
            elif c == ')':
                old_val, old_plus = stack.pop()
                val = old_val + (val if old_plus else -val)
                plus = True
            elif c == '+':
                plus = True
            elif c == '-':
                plus = False

        return val
