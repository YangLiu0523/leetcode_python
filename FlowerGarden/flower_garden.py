#!/usr/bin/python
# coding=utf-8
#
# Title:    Flower Garden from topcoder
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-20 16:47:35
#
class FlowerGarden(object):
    def getOrdering(self, height, bloom, wilt):
        def index_0(n):
            return n[0]
        sorted_param = sorted(zip(height, bloom, wilt), key=index_0)
        return self._getOrdering(
            [i[0] for i in sorted_param],
            [i[1] for i in sorted_param],
            [i[2] for i in sorted_param],
        )

    def _getOrdering(self, height, bloom, wilt, ret_h=[], ret_b=[], ret_w=[]):
        if height == []:
            return ret_h

        flower_h = height[0]
        flower_b = bloom[0]
        flower_w = wilt[0]
            
        i = len(ret_h) - 1
        while i >= 0:
            if flower_b > ret_w[i] or flower_w < ret_b[i]:            # satisfied 
                i -= 1
            else:
                break

        return self._getOrdering(
            height[1:], 
            bloom[1:], 
            wilt[1:],
            ret_h[:i + 1] + [flower_h] + ret_h[i + 1:],
            ret_b[:i + 1] + [flower_b] + ret_b[i + 1:],
            ret_w[:i + 1] + [flower_w] + ret_w[i + 1:],
        )

if __name__ == '__main__':
    h = [1, 2, 3, 4, 5, 6]
    b = [1, 3, 1, 3, 1, 3]
    w = [2, 4, 2, 4, 2, 4]
    assert(FlowerGarden().getOrdering(h, b, w) == [2, 4, 6, 1, 3, 5])
    h = [3, 2, 5, 4]
    b = [1, 2, 11, 10]
    w = [4, 3, 12, 13]
    assert(FlowerGarden().getOrdering(h, b, w) == [4, 5, 2, 3])
    h = [5, 4, 3, 2, 1]
    b = [1, 5, 10, 15, 20]
    w = [5, 10, 14, 20, 25]
    assert(FlowerGarden().getOrdering(h, b, w) == [3, 4, 5, 1, 2])
