import copy
class Solution(object):
    def CustomToBoard(self,testboard):
        board = []
        for i in range(9):
            board.append([])
            for j in range(9):
                board[i].append(testboard[i][j])
        return board

    def outputBoard(self,board):
        for i in range(9):
            for j in range(9):
                print board[i][j],
                if j%3 == 2:
                    print '',
            print 
            if i%3 == 2:
                print

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(9):
            exist = []
            for j in range(9):
                if board[i][j] in exist and board[i][j] != '.':
                    return False
                else:
                    exist.append(board[i][j])
            del exist
        
        for i in range(9):
            exist = []
            for j in range(9):
                if board[j][i] in exist and board[j][i] != '.':
                    return False
                else:
                    exist.append(board[j][i])
            del exist
        
        for m in range(0,7,3):
            for n in range(0,7,3):
                exist = []
                for i in range(m,m+3,1):
                    for j in range(n,n+3,1):
                        if board[i][j] in exist and board[i][j] != '.':
                            return False
                        else:
                            exist.append(board[i][j])
                del exist
        
        return True
    
    def judge(self,board):
        for i in board:
            if '.' in i:
                return False
        return True

    def solveSudoku(self,board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        boarder = {}
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
        ###
        for (i,j) in boarder:
            for x in boarder[(i,j)]:
                newboard = copy.deepcopy(board)
                newboard[i][j] = str(x)
                self.solveSudoku(newboard)
                if self.judge(newboard) and self.isValidSudoku(newboard):
                    break
            break
        if self.judge(newboard) and self.isValidSudoku(newboard):
            for i in range(9):
                for j in range(9):
                    board[i][j] = newboard[i][j]
        #print '\n',boarder,'\n'    
        return

if __name__ == '__main__':
    p = Solution()
    testboard = [
            "..9748...",
            "7........",
            ".2.1.9...",
            "..7...24.",
            ".64.1.59.",
            ".98...3..",
            "...8.3.2.",
            "........6",
            "...2759.."]
    board = Solution().CustomToBoard(testboard)
    Solution().outputBoard(board)

    Solution().solveSudoku(board)

    Solution().outputBoard(board)
