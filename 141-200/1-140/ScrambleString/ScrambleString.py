#!/usr/bin/python
# coding=utf-8
# 
# Date: 2017-11-02 12:16:12
# 
class Solution(object):
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        
        count = [0] * 26
        for i, j in zip(s1, s2):
            count[ord(i) - 97] += 1
            count[ord(j) - 97] -= 1
        for i in count:
            if i != 0:
                return False
        
        l = len(s1)
        for i in range(1, l):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[l-i:]) and self.isScramble(s1[i:], s2[:l-i]):
                return True
        return False
