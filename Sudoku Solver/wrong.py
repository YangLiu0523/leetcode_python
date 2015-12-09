class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        boarder = {}
        #初始化，标记所有可能结果
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    boarder[(i,j)] = [1,2,3,4,5,6,7,8,9]
        #print '\n',boarder,'\n'
        flag = True
        while flag:
            flag = False
            Return = True
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        Return = False
                        continue
                    value = int(board[i][j])
                    for m in range(9):
                        if (i,m) in boarder:
                            if value in boarder[(i,m)]:
                                del boarder[(i,m)][boarder[(i,m)].index(value)]
                                flag = True
                                if len(boarder[(i,m)]) == 1:
                                    board[i][m] = str(boarder[(i,m)][0])
                                    del boarder[(i,m)]
                    for m in range(9):
                        if (m,j) in boarder:
                            if value in boarder[(m,j)]:
                                del boarder[(m,j)][boarder[(m,j)].index(value)]
                                flag = True
                                if len(boarder[(m,j)]) == 1:
                                    board[m][j] = str(boarder[(m,j)][0])
                                    del boarder[(m,j)]
                    ii = i/3
                    jj = j/3
                    for m in range(3*ii, 3*ii+3, 1):
                        for n in range(3*jj, 3*jj+3 ,1):
                            if (m,n) in boarder:
                                if value in boarder[(m,n)]:
                                    del boarder[(m,n)][boarder[(m,n)].index(value)]
                                    flag = True
                                    if len(boarder[(m,n)]) == 1:
                                        board[m][n] = str(boarder[(m,n)][0])
                                        del boarder[(m,n)]
            #print '\n',boarder,'\n'
            if Return:
                return
        print '\n',boarder,'\n'    
