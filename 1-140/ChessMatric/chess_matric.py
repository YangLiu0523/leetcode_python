#!/usr/bin/python
# coding=utf-8
#
# Title:    Chess Matric
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-21 19:55:48
#
class ChessMatric(object):
    def howMany(self, size, start, finish, numMoves):
        chess = [[0] * size for _ in range(size)]
        chess[start[0]][start[1]] = 1
        for _ in range(numMoves):
            new_chess = [[0] * size for _ in range(size)]
            for i in range(size):
                for j in range(size):
                    if chess[i][j] == 0:
                        continue
                    cases = [
                        [i,j-1],
                        [i, j+1],
                        [i+1, j],
                        [i-1, j],
                        [i+1, j+1],
                        [i+1, j-1],
                        [i-1, j+1],
                        [i-1, j-1],

                        [i+1, j+2],
                        [i-1, j+2],
                        [i+1, j-2],
                        [i-1, j-2],
                        [i+2, j+1],
                        [i-2, j+1],
                        [i+2, j-1],
                        [i-2, j-1],
                    ]
                    for m, n in cases:
                        if m < 0 or n < 0 or m >= size or n >= size:
                            continue
                        new_chess[m][n] += chess[i][j]
            chess = new_chess
        return chess[finish[0]][finish[1]]


if __name__ == '__main__':
    print ChessMatric().howMany(
        100,
        [0, 0],
        [0, 99],
        50
    )
