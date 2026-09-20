class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while (s := numbers[l] + numbers[r]) != target:
            if s < target:
                l += 1
            else:
                r -= 1
        return [l + 1, r + 1]