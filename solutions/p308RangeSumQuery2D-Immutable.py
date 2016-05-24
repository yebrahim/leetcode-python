class NumMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                a = matrix[i-1][j] if i else 0
                b = matrix[i-1][j-1] if i and j else 0
                c = matrix[i][j-1] if j else 0
                matrix[i][j] += a+c-b

    def sumRegion(self, row1, col1, row2, col2):
        x = self.matrix[row2][col2]
        a = self.matrix[row1-1][col2] if row1 else 0
        b = self.matrix[row1-1][col1-1] if row1 and col1 else 0
        c = self.matrix[row2][col1-1] if col1 else 0
        return x - (a+c-b)
