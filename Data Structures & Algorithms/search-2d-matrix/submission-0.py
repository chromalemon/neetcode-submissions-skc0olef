class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m-1
        while left <= right:
            mid = (left+right)//2
            print(left, right)
            if matrix[mid][-1] < target:
                left = mid+1
            elif matrix[mid][0] > target:
                right = mid-1
            else:
                row = mid
                i, j = 0, n-1
                while i <= j:
                    mid = (i+j)//2
                    if matrix[row][mid] < target:
                        i = mid+1
                    elif matrix[row][mid] > target:
                        j = mid-1
                    else:
                        return True
                return False
        return False