#!/usr/bin/env python
# coding=utf-8
#
# Title: 174. Dungeon Game
# Author: Lucas
# Date: 2018-05-29 22:48:16
#
class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 0

        option_cache = [[] for _ in range(len(dungeon[0]))]
        option_cache[0] = [[1, 1]]
        for i in range(len(dungeon)):
            for j in range(len(dungeon[0])):
                # Possibilities
                options = option_cache[j] + option_cache[j-1] if j > 0 else option_cache[j]
                new_options = []
                for option in options:
                    new_option = [option[0], option[1] + dungeon[i][j]]
                    if new_option[1] < 1:
                        new_option = [new_option[0] + (1 - new_option[1]), 1]
                    new_options.append(new_option)
                # Remove useless
                flag = True
                while flag:
                    flag = False
                    for x in range(len(new_options)):
                        for y in range(len(new_options)):
                            if x == y:
                                continue
                            if new_options[x][0] >= new_options[y][0] and \
                                    new_options[x][1] <= new_options[y][1]:
                                del new_options[x]
                                flag = True
                                break
                        if flag:
                            break

                option_cache[j] = new_options
            # print(option_cache)

        min_cost = option_cache[-1][0][0]
        for option in option_cache[-1]:
            if option[0] < min_cost:
                min_cost = option[0]
        return min_cost
