class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        need = [0] * 128
        for char in t:
            need[ord(char)] += 1
            
        required = len(t)
        l = 0
        min_len = float('inf')
        min_start = 0
        
        for r, char in enumerate(s):
            if need[ord(char)] > 0:
                required -= 1
            
            need[ord(char)] -= 1
            
            while required == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_start = l
                    
                left_char = s[l]
                need[ord(left_char)] += 1
                
                if need[ord(left_char)] > 0:
                    required += 1
                    
                l += 1
                
        return "" if min_len == float('inf') else s[min_start:min_start + min_len]