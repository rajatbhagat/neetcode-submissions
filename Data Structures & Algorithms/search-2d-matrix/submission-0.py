class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        location = -1
        for i in range(rows):
            if matrix[i][0] == target:
                return True
            if matrix[i][0] < target:
                location = i
        left = 0
        right = len(matrix[location]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[location][mid]:
                return True
            elif target > matrix[location][mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False
