class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:
            val = num % k
            new_dp = [0] * k
            for r in range(k):
                if dp[r] > 0:
                    new_dp[(r * val) % k] += dp[r]
            new_dp[val] += 1

            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result