class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len = 0
        start = 0
        
        for i, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            
            seen[char] = i
            length = i - start + 1
            
            if length > max_len:
                max_len = length
                
        return max_len