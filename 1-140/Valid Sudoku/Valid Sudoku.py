class Solution(object):
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
