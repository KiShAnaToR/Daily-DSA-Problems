class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = max_sum = sum(nums[:k])
        
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        return max_sum / k