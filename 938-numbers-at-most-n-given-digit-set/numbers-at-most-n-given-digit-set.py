class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        m = len(digits)
        ans = 0

        for length in range(1, len(s)):
            ans += m ** length

        for i, ch in enumerate(s):
            smaller = 0

            for d in digits:
                if d < ch:
                    smaller += 1
                else:
                    break

            ans += smaller * (m ** (len(s) - i - 1))

            if ch not in digits:
                return ans

        return ans + 1