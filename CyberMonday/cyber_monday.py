#!/usr/bin/python
# coding=utf-8
#
# Title:    Cyber Monday from Company Bot
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-09-04 20:31:18
#
import copy
def _to_int(s_t):
    s_t = s_t.split(':')
    return int(s_t[0]) * 60 + int(s_t[1])


def solution(shoppers, orders, leadTime):
    shoppers = [[_to_int(i), _to_int(j)] for i, j in shoppers]
    orders = [[_to_int(i), _to_int(j)] for i, j in orders]
    order_shoppers = []
    
    for order, lead_time in zip(orders, leadTime):
        order_shopper = []
        for shopper in shoppers:
            if max(order[0], shopper[0]) + lead_time <= min(order[1], shopper[1]):
                order_shopper.append(shopper)
        order_shoppers.append(order_shopper)
    return _solution(orders, order_shoppers)


def _solution(orders, order_shoppers):
    if not orders:
        return True

    for i in range(len(orders)):
        if not order_shoppers[i]:
            return False
        for j in range(len(order_shoppers[i])):
            new_shoppers = copy.deepcopy(order_shoppers)
            order = order_shoppers[i][j]
            for ss in new_shoppers:
                if order in ss:
                    ss.remove(order_shoppers[i][j])
            if _solution(orders[:i] + orders[i+1:], new_shoppers):
                return True
    return False


if __name__ == '__main__':
    s = [["23:00","23:59"], 
         ["22:30","23:30"]]
    o = [["23:15","23:35"], 
         ["23:00","23:31"]]
    l = [20, 31]
    print solution(s, o, l)
