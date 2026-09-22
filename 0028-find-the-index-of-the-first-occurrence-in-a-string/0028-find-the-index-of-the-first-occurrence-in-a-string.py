class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(needle), len(haystack)
        
        lps = [0] * m
        length = 0
        i = 1
        
        while i < m:
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
                    
        i = 0
        j = 0
        
        while i < n:
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            
            if j == m:
                return i - j
            elif i < n and needle[j] != haystack[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
                    
        return -1