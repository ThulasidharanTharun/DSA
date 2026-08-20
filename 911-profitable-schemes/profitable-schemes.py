class Solution:
    def profitableSchemes(
        self,
        n: int,
        minProfit: int,
        group: List[int],
        profit: List[int]
    ) -> int:
        
        MOD = 10**9 + 7

        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]

        dp[0][0] = 1

        for members_needed, crime_profit in zip(group, profit):

            for members in range(n, members_needed - 1, -1):
                for p in range(minProfit, -1, -1):

                    new_profit = min(
                        minProfit,
                        p + crime_profit
                    )

                    dp[members][new_profit] = (
                        dp[members][new_profit]
                        + dp[members - members_needed][p]
                    ) % MOD

        return sum(dp[members][minProfit] for members in range(n + 1)) % MOD