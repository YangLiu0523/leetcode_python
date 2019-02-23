# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-23 10:56:09


import string


class Solution:
    def calculate(self, s: 'str') -> 'int':
        s = s.replace(' ', '')
        queue = []
        val = 1
        num = ''
        flag = True

        for c in s + '\0':
            if c in string.digits:
                num = num + c
            else:
                if flag == True:
                    val = val * int(num)
                else:
                    val = val // int(num)
                num = ''

            if c == '*':
                flag = True
            elif c == '/':
                flag = False
            elif c == '+':
                queue.append((val, c))
                val, flag = 1, True
            elif c == '-':
                queue.append((val, c))
                val, flag = 1, True
            elif c == '\0':
                queue.append((val, c))

        flag = True
        val = 0
        for num, c in queue:
            if flag:
                val += num
            else:
                val -= num

            if c == '+':
                flag = True
            else:
                flag = False

        return val
