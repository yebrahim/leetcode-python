class Solution(object):
    def isValidSudoku(self, board):
        nums=set(['1','2','3','4','5','6','7','8','9'])

        def getsquare(i):
            r,c=divmod(i,3)
            l=[]
            r*=3; c*=3
            for __r in range(r,3+r):
                for __c in range(c,3+c):
                    if board[__r][__c] != '.': l.append(board[__r][__c])
            return l

        for i in range(9):
            row=[c for c in board[i] if c != '.']
            rowset=set(row)
            col=[c for c in zip(*board)[i] if c != '.']
            colset=set(col)
            squ=getsquare(i)
            squset=set(squ)
            if len(rowset) != len(row) or not rowset.issubset(nums): return False
            if len(colset) != len(col) or not colset.issubset(nums): return False
            if len(squset) != len(squ) or not squset.issubset(nums): return False
        return True