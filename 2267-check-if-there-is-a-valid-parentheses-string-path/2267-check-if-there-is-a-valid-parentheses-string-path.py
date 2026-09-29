"""
I used the help of AI in this question; I got stuck on this part:
pruning the search space by tracking the open/close parenthesis balance at each cell (r, c, bal)
and realizing that if the path length m + n - 1 is odd or the remaining steps are less than the
current balance, the path is immediately invalid.
"""

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
        
        if grid[0][0] != '(' or grid[m - 1][n - 1] != ')':
            return False

        dp = [0] * n
        dp[0] = 1

        for r in range(m):
            new_dp = [0] * n
            for c in range(n):
                if r == 0 and c == 0:
                    mask = dp[0]
                else:
                    mask = 0
                    if r > 0:
                        mask |= dp[c]
                    if c > 0:
                        mask |= new_dp[c - 1]
                
                if mask == 0:
                    continue

                if grid[r][c] == '(':
                    mask <<= 1
                else:
                    mask >>= 1

                rem = (m - 1 - r) + (n - 1 - c)
                mask &= (1 << (rem + 1)) - 1
                new_dp[c] = mask
            dp = new_dp

        return bool(dp[-1] & 1)