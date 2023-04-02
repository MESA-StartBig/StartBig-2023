class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1], [1, 1]]
        if numRows == 1 or numRows == 2:
            return triangle[:numRows]
            
        for i in range(2, numRows):
            row_len = i+1
            row = [1] * row_len
            for j in range(1, row_len - 1):
                row[j] = triangle[-1][j-1] + triangle[-1][j]
            triangle.append(row)

        return triangle