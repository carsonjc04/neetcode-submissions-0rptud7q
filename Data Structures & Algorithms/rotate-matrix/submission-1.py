class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # matrix = [[1,2], [3,4]]
        # matrix = [[1,2,3], [4,5,6], [7,8,9]]
        # botL, botR, topR, topL
        # temp = topL
        # [1,2,3]
        # [4,5,6]
        # [7,8,9]

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bot = l, r

                topLeft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bot - i][l]

                matrix[bot - i][l] = matrix[bot][r - i]

                matrix[bot][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topLeft
            l += 1
            r -= 1



