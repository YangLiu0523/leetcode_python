#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-12-14 16:54:09
# 

class Solution(object):
    def _visit(self, board, i, j, queue):
        print i, j
        if board[i][j] == 'O':
            queue.append([i, j])
            board[i][j] = 'M'
    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        l1 = len(board)
        l2 = len(board[0])
        
        queue = []
        for i in range(l1):
            for j in [0, l2-1]:
                self._visit(board, i, j, queue)
        for i in [0, l1-1]:
            for j in range(l2):
                self._visit(board, i, j, queue)
                
        while queue:
            new_queue = []
            for i, j in queue:
                if i+1 < l1:
                    self._visit(board, i+1, j, new_queue)
                if i-1 >= 0:
                    self._visit(board, i-1, j, new_queue)
                if j+1 < l2:
                    self._visit(board, i, j+1, new_queue)
                if j-1 >= 0:
                    self._visit(board, i, j-1, new_queue)
            queue = new_queue
        
        for i in range(l1):
            for j in range(l2):
                board[i][j] = 'O' if board[i][j] == 'M' else 'X'
                        
