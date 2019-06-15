#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-15 22:38:52


class Solution(object):
    def _dfs(self, fs, index):
        if index >= len(fs):
            return [""]
        tmp = self._dfs(fs, index + 1)
        ans = []
        for opt in fs[index]:
            for t in tmp:
                ans.append(opt + t)
        return ans

    def permute(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        fs = []
        bra = False
        for c in S:
            if not bra and c != '{':
                fs.append([c])
            elif not bra and c == '{':
                fs.append([])
                bra = True
            elif bra and c != '}':
                if c == ',':
                    continue
                fs[-1].append(c)
            elif bra and c == '}':
                bra = False

        for opts in fs:
            opts.sort()

        return self._dfs(fs, 0)


def main():
    testcases = [
        ("{a,b}c{d,e}f", ["acdf","acef","bcdf","bcef"]),
        ("abcd", ["abcd"])
    ]
    for case, target in testcases:
        print(Solution().permute(case), target)


if __name__ == '__main__':
    main()
