class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        find mid row
        Compare left to target, 

        """

        l,r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                break
        
        row = (l + r) // 2

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False