#!/usr/bin/python
# coding=utf-8
#
# Title:    Avoid Roads from TopCoder
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-21 10:12:02
#
class AvoidRoads(object):
    def numWays(self, width, height, bad):
        for i in range(len(bad)):
            nums = [int(j) for j in bad[i].split(' ')]
            if nums[2] < nums[0] or nums[3] < nums[1]:
                bad[i] = '%d %d %d %d' % (nums[2], nums[3], nums[0], nums[1])

        solutions = []
        for i in range(width + 1):
            solutions.append([])
            for j in range(height + 1):
                if i == 0 and j == 0:
                    solutions[i].append(1)
                    continue
                
                # for m in solutions:
                    # for n in m:
                        # print n, '\t',
                    # print ''
                # raw_input('%d, %d' % (i, j))
                # print '%d, %d' % (i, j)

                solutions[i].append(
                    (solutions[i][j - 1] if ((j > 0) and ('%d %d %d %d' % (i, j - 1, i, j) not in bad)) else 0) + \
                    (solutions[i - 1][j] if ((i > 0) and ('%d %d %d %d' % (i - 1, j, i, j) not in bad)) else 0)  
                )
        return solutions[-1][-1]


if __name__ == '__main__':
    # print AvoidRoads().numWays(1, 1, [])
    # print AvoidRoads().numWays(6, 6, ["0 0 0 1", "6 6 5 6"])
    print AvoidRoads().numWays(35, 31, [])
