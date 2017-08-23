#!/usr/bin/python
# coding=utf-8
#
# Title:    Jewelry from TopCoder
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-22 23:11:42
#
class Jewelry(object):
    def howMany(self, values):
        values.sort()
        solutions = [[[], []]]
        ret = []
        for jewelry in values:
            new_solutions = []
            for solution in solutions:
                new_solutions.append([
                    solution[0],
                    solution[1] + [jewelry]
                ])
                if not solution[1] or jewelry <= solution[1][-1]:
                    new_solutions.append([
                        solution[0] + [jewelry],
                        solution[1]
                    ])
            for solution in new_solutions:
                if solution[0] and solution[1] and solution[0][-1] <= solution[1][0]:
                    solutions.append(solution)
                    if sum(solution[0]) == sum(solution[1]):
                        ret.append(solution)
            solutions = new_solutions + solutions
        return len(ret)


if __name__ == '__main__':
    # cases = [1, 2, 5, 3, 4, 5]
    cases = [1, 2, 3, 4, 5, 5]
    # cases = [
        # 1000, 1000, 1000, 1000, 1000,
        # 1000, 1000, 1000, 1000, 1000,
        # 1000, 1000, 1000, 1000, 1000,
        # 1000, 1000, 1000, 1000, 1000,
        # 1000, 1000, 1000, 1000, 1000,
        # 1000, 1000, 1000, 1000, 1000,
    # ]
    print Jewelry().howMany(cases)
