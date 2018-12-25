#!/usr/bin/python
# coding=utf-8
#
# Title:    Bad Neighbors
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-19 23:31:34
#
class BadNeighbors(object):
    def maxDonations(self, donations):
        return max(self._maxDonations(donations[1:]), self._maxDonations(donations[:-1]))

    def _maxDonations(self, donations):
        m = m_neighbors = 0

        for i in donations:
            m, m_neighbors = m_neighbors, max(m + i, m_neighbors)
            print i, m, m_neighbors
        print ''
        return max(m, m_neighbors)


if __name__ == '__main__':
    # cases = [10, 3, 2, 5, 7, 8]
    cases = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    # cases = [7, 7, 7, 7, 7, 7, 7]
    # cases = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
             # 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
             # 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]
    print BadNeighbors().maxDonations(cases)
