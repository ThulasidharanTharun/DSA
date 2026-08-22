class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        result = 0

        for i in range(n):
            result += nums[i] * (
                pow(2, i, MOD) - pow(2, n - 1 - i, MOD)
            )

        return result % MOD