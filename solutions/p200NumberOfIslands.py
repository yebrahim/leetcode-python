class Solution(object):
    def __traverseOnes(self, r, c):
        self.__grid[r][c] = '2'
        if r>0 and self.__grid[r-1][c]=='1': self.__traverseOnes(r-1,c)
        if r+1<len(self.__grid) and self.__grid[r+1][c]=='1': self.__traverseOnes(r+1,c)
        if c>0 and self.__grid[r][c-1]=='1': self.__traverseOnes(r,c-1)
        if c+1<len(self.__grid[0]) and self.__grid[r][c+1]=='1': self.__traverseOnes(r,c+1)
        
    def numIslands(self, grid):
        self.__grid = grid
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.__traverseOnes(i,j)
                    islands+=1
        return islands