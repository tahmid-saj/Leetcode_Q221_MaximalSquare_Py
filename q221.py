class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        return self.bottomUp(matrix)
    
    def bottomUp(self, matrix):
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        maxLength = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0: dp[i][j] = 1
                    else: dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
                    maxLength = max(maxLength, dp[i][j])
        return maxLength * maxLength
