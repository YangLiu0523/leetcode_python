#!/usr/bin/python
# coding=utf-8
#
# Title: 135. Candy
# Author: Lucas
# Date: 2018-04-16 22:20:09
#
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) == 1:
            return 1
        if len(ratings) == 2:
            return 3 - int(ratings[0] == ratings[1])

        local_minimum = []
        if ratings[0] < ratings[1]:
            local_minimum.append(0)
        if ratings[-2] > ratings[-1]:
            local_minimum.append(len(ratings)-1)
        for index in range(1, len(ratings) - 1):
            if ratings[index-1] >= ratings[index] and ratings[index] <= ratings[index+1]:
                local_minimum.append(index)

        candies = [1] * len(ratings)
        for index in local_minimum:
            left = index - 1
            right = index + 1
            while left >= 0 and ratings[left] > ratings[left+1]:
                candies[left] = max(candies[left], candies[left+1]+1)
                left -= 1
            while right < len(ratings) and ratings[right-1] < ratings[right]:
                candies[right] = max(candies[right], candies[right-1]+1)
                right += 1
        return sum(candies)
