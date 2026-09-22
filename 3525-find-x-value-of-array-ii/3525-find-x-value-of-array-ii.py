class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        tree_prod = [1] * (2 * n)
        tree_count = [[0] * k for _ in range(2 * n)]
        
        for i in range(n):
            v = nums[i] % k
            tree_prod[n + i] = v
            tree_count[n + i][v] = 1
            
        for i in range(n - 1, 0, -1):
            left = i << 1
            right = left | 1
            tree_prod[i] = (tree_prod[left] * tree_prod[right]) % k
            lp = tree_prod[left]
            for j in range(k):
                tree_count[i][j] = tree_count[left][j]
            for j in range(k):
                if tree_count[right][j]:
                    tree_count[i][(lp * j) % k] += tree_count[right][j]
                    
        ans = []
        
        for idx, val, st, x in queries:
            p = idx + n
            v = val % k
            tree_prod[p] = v
            for j in range(k):
                tree_count[p][j] = 0
            tree_count[p][v] = 1
            
            p >>= 1
            while p > 0:
                left = p << 1
                right = left | 1
                tree_prod[p] = (tree_prod[left] * tree_prod[right]) % k
                lp = tree_prod[left]
                for j in range(k):
                    tree_count[p][j] = tree_count[left][j]
                for j in range(k):
                    if tree_count[right][j]:
                        tree_count[p][(lp * j) % k] += tree_count[right][j]
                p >>= 1
                
            l = st + n
            r = 2 * n
            left_nodes = []
            right_nodes = []
            
            while l < r:
                if l & 1:
                    left_nodes.append(l)
                    l += 1
                if r & 1:
                    r -= 1
                    right_nodes.append(r)
                l >>= 1
                r >>= 1
                
            ans_counts = [0] * k
            curr_p = 1
            
            for node in left_nodes:
                for j in range(k):
                    if tree_count[node][j]:
                        ans_counts[(curr_p * j) % k] += tree_count[node][j]
                curr_p = (curr_p * tree_prod[node]) % k
                
            for i in range(len(right_nodes) - 1, -1, -1):
                node = right_nodes[i]
                for j in range(k):
                    if tree_count[node][j]:
                        ans_counts[(curr_p * j) % k] += tree_count[node][j]
                curr_p = (curr_p * tree_prod[node]) % k
                
            ans.append(ans_counts[x])
            
        return ans