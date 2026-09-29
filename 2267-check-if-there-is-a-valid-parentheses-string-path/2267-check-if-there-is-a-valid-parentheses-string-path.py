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
            
        visited = set()
        queue = [(0, 0, 1)]
        visited.add((0, 0, 1))
        
        while queue:
            r, c, bal = queue.pop(0)
            
            if r == m - 1 and c == n - 1:
                if bal == 0:
                    return True
                continue
            
            remaining_steps = (m - 1 - r) + (n - 1 - c)
            if bal > remaining_steps:
                continue
                
            for dr, dc in [(1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if nr < m and nc < n:
                    delta = 1 if grid[nr][nc] == '(' else -1
                    next_bal = bal + delta
                    
                    if next_bal >= 0 and (nr, nc, next_bal) not in visited:
                        visited.add((nr, nc, next_bal))
                        queue.append((nr, nc, next_bal))
                        
        return False