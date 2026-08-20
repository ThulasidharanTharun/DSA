class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        index = {num: i for i, num in enumerate(arr)}
        dp = {}
        ans = 0
        for j in range(n):
            for k in range(j + 1, n):
                prev = arr[k] - arr[j]
                if prev < arr[j] and prev in index:
                    i = index[prev]
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    ans = max(ans, dp[(j, k)])
        return ans if ans >= 3 else 0