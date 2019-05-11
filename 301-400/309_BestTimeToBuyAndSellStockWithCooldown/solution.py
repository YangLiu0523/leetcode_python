#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-11 12:29:58


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        with_sell, with_keep, without_buy, without_keep = 0, -prices[0], -prices[0], 0
        for price in prices:
            with_keep = max(with_keep, without_buy)
            without_buy = without_keep - price
            without_keep = max(with_sell, without_keep)
            with_sell = with_keep + price

        return max(with_sell, without_keep)
