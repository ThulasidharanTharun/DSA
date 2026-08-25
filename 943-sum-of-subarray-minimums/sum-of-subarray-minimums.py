class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        result = 0

        for i in range(n + 1):
            curr = arr[i] if i < n else 0

            while stack and arr[stack[-1]] > curr:
                mid = stack.pop()
                left = stack[-1] if stack else -1

                left_count = mid - left
                right_count = i - mid

                result += arr[mid] * left_count * right_count

            stack.append(i)

        return result % MOD