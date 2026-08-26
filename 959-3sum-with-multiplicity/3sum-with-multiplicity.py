class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        arr.sort()
        n = len(arr)
        ans = 0

        for i in range(n):
            left, right = i + 1, n - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    # All elements between left and right are equal
                    if arr[left] == arr[right]:
                        count = right - left + 1
                        ans += count * (count - 1) // 2
                        break

                    # Count duplicates on both sides
                    left_count = 1
                    right_count = 1

                    while left + 1 < right and arr[left] == arr[left + 1]:
                        left_count += 1
                        left += 1

                    while right - 1 > left and arr[right] == arr[right - 1]:
                        right_count += 1
                        right -= 1

                    ans += left_count * right_count
                    left += 1
                    right -= 1

        return ans % MOD