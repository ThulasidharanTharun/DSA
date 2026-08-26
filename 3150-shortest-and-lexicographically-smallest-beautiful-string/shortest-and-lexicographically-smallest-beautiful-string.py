class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']

        if len(ones) < k:
            return ""

        ans = ""

        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]

            # Include zeros after the kth '1' only if needed for the next window,
            # so the shortest substring ends at the kth '1'
            curr = s[left:right + 1]

            if ans == "" or len(curr) < len(ans) or (
                len(curr) == len(ans) and curr < ans
            ):
                ans = curr

        return ans