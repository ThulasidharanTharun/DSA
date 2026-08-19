class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            d = 3
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 2

            return True
        for x in range(max(2, n), 10):
            if is_prime(x):
                return x

        length = len(str(n))

        while True:
            half = (length + 1) // 2

            for first in range(10 ** (half - 1), 10 ** half):
                s = str(first)

                if length % 2 == 0:
                    pal = int(s + s[::-1])
                else:
                    pal = int(s + s[-2::-1])

                if pal >= n and is_prime(pal):
                    return pal

            length += 1