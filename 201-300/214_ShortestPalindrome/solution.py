# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-13 21:46:34


class Solution:
    def shortestPalindrome(self, s: 'str') -> 'str':
        s = ' '.join(s)
        mid = len(s) // 2
        while True:
            s1 = s[:mid]
            if s1[::-1] == s[mid + 1:mid + len(s1) + 1]:
                break
            mid -= 1

        left = s[mid:]
        return (left[::-1][:-1] + left).replace(' ', '')
