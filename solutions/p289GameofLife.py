class Solution(object):
    def _countneighbors(self, board, i, j):
        count = 0
        for p in range (max(i-1, 0), min(i+2, len(board))):
            for q in range(max(j-1,0), min (j+2, len(board[0]))):
                if p!=i or q!=j:
                    count += (1 if board[p][q] in [1,2] else 0)
        return count
        
    def _fixboard(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] %= 2

    def gameOfLife(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = self._countneighbors(board, i, j)
                if board[i][j] in [1,3] and (c < 2 or c > 3): board[i][j] = 2
                if board[i][j] in [0,2] and c == 3: board[i][j] = 3
        self._fixboard(board)
