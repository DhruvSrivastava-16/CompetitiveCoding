class Solution:
    def rotate(self, matrix):
        l = matrix
        matrix[0][0] = 9099
        l[1][1] = 22837

     
S = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
S.rotate(matrix)
