# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-21 23:22:51

class Solution:
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        areaa = (ax2 - ax1) * (ay2 - ay1)
        areab = (bx2 - bx1) * (by2 - by1)

        # Intersect but not contain
        width = self._sect(ax1, ax2, bx1, bx2)
        height = self._sect(ay1, ay2, by1, by2)
        return areaa + areab - width * height

    def _sect(self, i1, i2, j1, j2):
        if j2 <= i1:
            return 0
        if i2 <= j1:
            return 0
        if i1 <= j1 <= j2 <= i2:
            return j2 - j1
        if j1 <= i1 <= i2 <= j2:
            return i2 - i1

        if i1 <= j1 <= i2:
            return i2 - j1
        if i1 <= j2 <= i2:
            return j2 - i1
