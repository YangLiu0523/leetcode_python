class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                live_neighbor = 0
                for n in range(max(i-1, 0), min(i+2, len(board))):
                    for m in range(max(j-1, 0), min(j+2, len(board[i]))):
                        if n == i and m == j:
                            continue
                        if board[n][m] & 1 == 1:
                            live_neighbor += 1
                
                if board[i][j] & 1 == 1 and live_neighbor in (2, 3):
                    board[i][j] += 2
                if board[i][j] & 1 == 0 and live_neighbor == 3:
                    board[i][j] += 2
                    
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = board[i][j] // 2
