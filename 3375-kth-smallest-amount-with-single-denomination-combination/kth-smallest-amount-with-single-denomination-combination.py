from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        
        coins.sort()
        filtered = []
        
        for coin in coins:
            if not any(coin % prev == 0 for prev in filtered):
                filtered.append(coin)
        
        coins = filtered
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                cur_lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        cur_lcm = lcm(cur_lcm, coins[i])
                        bits += 1

                        if cur_lcm > x:
                            break

                if cur_lcm > x:
                    continue

                multiples = x // cur_lcm

                if bits % 2 == 1:
                    total += multiples
                else:
                    total -= multiples

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left