class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # for row in matrix:
        #     if target in row: 
        #         return True 
        # return False

        m = len(matrix[0])
        n = len(matrix)

        l , r = 0, n - 1

        while(l <= r):

            mr = l + ((r-l) // 2)
            if target in matrix[mr]:
                return True
            if target > matrix[mr][-1]:
                l = mr + 1
            else:
                r = mr - 1
        return False
    