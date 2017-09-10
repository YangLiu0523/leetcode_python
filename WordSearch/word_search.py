#!/usr/bin/python
# coding=utf-8
#
# Title:    Word Search
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-09-10 23:23:26
#
class Solution(object):
    def exist(self, board, word):
        ways = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    ways.append([[i, j]])
        
        for c in word[1:]:
            new_ways = []
            
            for way in ways:
                i, j = way[-1]
                if i - 1 >= 0 and board[i-1][j] == c and [i-1, j] not in way:
                    new_ways.append(way + [[i-1, j]])
                if i + 1 < len(board) and board[i+1][j] == c and [i+1, j] not in way:
                    new_ways.append(way + [[i+1, j]])
                if j - 1 >= 0 and board[i][j-1] == c and [i, j-1] not in way:
                    new_ways.append(way + [[i, j-1]])
                if j + 1 < len(board[0]) and board[i][j+1] == c and [i, j+1] not in way:
                    new_ways.append(way + [[i, j+1]])
            ways = new_ways
        
        return not (ways == [])
        
