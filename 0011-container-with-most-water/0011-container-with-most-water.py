class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            w = right - left
            hl, hr = height[left], height[right]
            if hl < hr:
                area = w * hl
                left += 1
            else:
                area = w * hr
                right -= 1
            if area > res:
                res = area
        return res