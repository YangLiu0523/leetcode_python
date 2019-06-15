#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-15 22:51:15
"""
5 ** 9 = 1953125
"""


class Solution(object):
    mapping = {
        1: 1,
        6: 9,
        9: 6,
        0: 0,
        8: 8
    }
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        spe = (0, 1, 6, 8, 9)
        max_n = []
        eq = True
        for i in str(N):
            i = int(i)
            if eq and i in spe:
                max_n.append(i)
            elif not eq:
                max_n.append(9)
            else:
                max_n.append(max([j for j in spe if j < i]))
                eq = False
        # print(max_n)

        # with rotated
        ans = 1
        l = len(max_n) - 1
        for i in max_n:
            ans += (5 ** l) * spe.index(i)
            l -= 1
        # print(ans)

        rotated = 0
        l = len(max_n)
        index = [0] * len(max_n)
        while True:
            num = int(''.join([str(spe[i]) for i in index]))
            if num > N:
                break
            if num == N:
                rotated += 1
                break
            rotated += 1
            print(num)
            if len(index) % 2 == 0:
                index[l // 2 - 1] += 1
            elif len(index) % 2 == 1:
                next_i = {
                    0: 1,
                    1: 3,
                    3: 5
                }
                index[l // 2] = next_i[index[l // 2]]
            i = (l - 1) // 2
            while index[i] >= 5 and i != 0:
                index[i-1] += 1
                index[i] -= 5
                i -= 1
            if index[0] == 5:
                break
            for i in range((l - 1) // 2 + 1):
                index[-(i + 1)] = spe.index(self.mapping[spe[index[i]]])
        return ans - rotated


def main():
    cases = [
        618
        # 1000000000
    ]
    for case in cases:
        print(case, Solution().confusingNumberII(case))


if __name__ == '__main__':
    main()
