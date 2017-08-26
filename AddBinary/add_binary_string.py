#!/usr/bin/python
# coding=utf-8
#
# Title:    Add Binary String Solution
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-26 21:35:46
#
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        else:
            a = '0' * (len(b) - len(a)) + a
        
        flag = '0'
        ret = ''
        for i, j in zip(a[::-1], b[::-1]):
            c = [i, j, flag].count('1')
            ret = str(c % 2) + ret
            flag = str(c / 2)
        return '1' + ret if flag == '1' else ret
