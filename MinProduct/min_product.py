#!/usr/bin/python
# coding=utf-8
#
# Title:    Min Product From TopCoder
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-24 19:42:47
#
class MinProduct(object):
    def findMin(self, amount, blank1, blank2):
        choises = []
        for index, value in zip(range(10), amount):
            choises += [index] * value
        a = choises[0]
        b = choises[1]
        choises = choises[2:blank1+blank2]
        return self._reverse(choises, a, b, blank1, blank2)
    
    def _reverse(self, choises, a, b, blank1, blank2):
        if not choises:
            return a * b

        # for index, i in zip(range(len(choises), choises)):
        min_mul1 = min_mul2 = None
        if blank1 > 1:
            min_mul1 = min([self._reverse(
                    choises[:index] + choises[index+1:], 
                    a * 10 + value,
                    b,
                    blank1 - 1, blank2) for index, value in zip(range(len(choises)), choises)])
        
        if blank2 > 1:
            min_mul2 = min([self._reverse(
                    choises[:index] + choises[index+1:], 
                    a,
                    b * 10 + value,
                    blank1,
                    blank2 - 1) for index, value in zip(range(len(choises)), choises)])

        if min_mul1 is None:
            return min_mul2
        elif min_mul2 is None:
            return min_mul1
        return min(min_mul1, min_mul2) 


if __name__ == '__main__':
    print MinProduct().findMin([0,1,1,2,1,1,0,0,0,0], 2, 3)
