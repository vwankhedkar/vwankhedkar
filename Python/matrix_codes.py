# Time:  O(m * n)
# Space: O(m * n)

# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up 
# or down. You may NOT move diagonally or move outside of the boundary 
# (i.e. wrap-around is not allowed).
#
# Example 1:
#
# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Return 4
# The longest increasing path is [1, 2, 6, 9].
#
# Example 2:
#
# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Return 4
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

# DFS + Memorization solution.
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0

        def longestpath(matrix, i, j, max_lengths):
            if max_lengths[i][j]:
                return max_lengths[i][j]
        
            max_depth = 0
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for d in directions:
                x, y = i + d[0], j + d[1]
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and \
                   matrix[x][y] < matrix[i][j]:
                    max_depth = max(max_depth, longestpath(matrix, x, y, max_lengths));
            max_lengths[i][j] = max_depth + 1
            return max_lengths[i][j]

        res = 0
        max_lengths = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, longestpath(matrix, i, j, max_lengths))
        return res
      
nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]]
print(Solution().longestIncreasingPath(nums))

OUTPUT: 4
************************************************************************************
def matrix_reverse(s, n=4):
    matrix = [[None]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = s[index]
            index += 1
    for row in matrix:
        print(row[:])
    print("Final Reverse matrix is : ")
    for row in matrix:
        print(row[::-1])
        
matrix_reverse("ABCDEFGHIJKLMNOP", 4)
['A', 'B', 'C', 'D']
['E', 'F', 'G', 'H']
['I', 'J', 'K', 'L']
['M', 'N', 'O', 'P']
Final Reverse matrix is : 
['D', 'C', 'B', 'A']
['H', 'G', 'F', 'E']
['L', 'K', 'J', 'I']
['P', 'O', 'N', 'M']
