class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = 0
        
        for stone in stones:
            prefix += stone
        
        dp = prefix

        for i in range(len(stones) - 2, 0, -1):
            prefix -= stones[i + 1]
            dp = max(dp, prefix - dp)

        return dp